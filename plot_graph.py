import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from partx.models.partx_options import partx_options
import pathlib
import pickle
import matplotlib.pyplot as plt
import math
from matplotlib.font_manager import FontProperties
from partx.numerical.sampling import uniform_sampling
from sklearn.gaussian_process import GaussianProcessRegressor
from scipy import stats

def save_trees_plots(q, tree_dir, im_dir, options):
    print(q)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    f = open(tree_dir, "rb")
    ftree = pickle.load(f)
    f.close()

    leaves = ftree.leaves()
    # print("*******************************************************")
    
    for x,i in enumerate(leaves):
        print(x)
        # fig = plt.figure()
        # x_1, y_1, x_2,y_2,x_3,y_3,x_4,y_4 = plotRegion(i.data.region_support)
        r_support = np.array(i.data.region_support)
        regionBounds_x_min = r_support[0][0][0]
        regionBounds_x_max = r_support[0][0][1]
        regionBounds_y_min = r_support[0][1][0]
        regionBounds_y_max = r_support[0][1][1]
        regionBounds_z_min = r_support[0][2][0]
        regionBounds_z_max = r_support[0][2][1]

        x = np.linspace(regionBounds_x_min, regionBounds_x_max, num=10)
        y = np.linspace(regionBounds_y_min, regionBounds_y_max,num=10)
        z = np.linspace(regionBounds_z_min, regionBounds_z_max,num=10)

        
        x1, z1 = np.meshgrid(x, z)
        y11 = np.ones_like(x1)*(r_support[0][1][0])
        y12 = np.ones_like(x1)*(r_support[0][1][1])
        x2, y2 = np.meshgrid(x, y)
        z21 = np.ones_like(x2)*(r_support[0][2][0])
        z22 = np.ones_like(x2)*(r_support[0][2][1])
        y3, z3 = np.meshgrid(y, z)
        x31 = np.ones_like(y3)*(r_support[0][0][0])
        x32 = np.ones_like(y3)*(r_support[0][0][1])
        
        if i.data.region_class == "+":
            col = "green"
            alpha = 0.5
        if i.data.region_class == "-":
            print(i.data.region_class)
            col = "red"
            alpha = 0.9
        if i.data.region_class == "r" or i.data.region_class == "r+" or i.data.region_class == "r-":
            col = "blue"
            alpha = 0.2
        # ax.hold(True)
        # ax = fig.gca(projection='3d')
        # outside surface
        ax.plot_surface(x1, y11, z1, color=col, rstride=1, cstride=1, alpha=alpha)
        # inside surface
        ax.plot_surface(x1, y12, z1, color=col, rstride=1, cstride=1,  alpha=alpha)
        # bottom surface
        ax.plot_surface(x2, y2, z21, color=col, rstride=1, cstride=1,  alpha=alpha)
        # upper surface
        ax.plot_surface(x2, y2, z22, color=col, rstride=1, cstride=1,  alpha=alpha)
        # left surface
        ax.plot_surface(x31, y3, z3, color=col, rstride=1, cstride=1,  alpha=alpha)
        # right surface
        ax.plot_surface(x32, y3, z3,  color=col, rstride=1, cstride=1,  alpha=alpha)
        ax.grid(False)
    # plt.show()
    ax.set_xlim(options.initial_region_support[0][0][0], options.initial_region_support[0][0][1])
    ax.set_ylim(options.initial_region_support[0][1][0], options.initial_region_support[0][1][1])
    ax.set_zlim(options.initial_region_support[0][2][0], options.initial_region_support[0][2][1])
    plt.savefig(im_dir, dpi = 400)


def generate_scatterplot(number_of_samples, q, im_dir, options, model, rng):
    print(q)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    

    samples = uniform_sampling(number_of_samples, options.initial_region_support, options.test_function_dimension, rng)
    y_pred, sigma_st = model.predict(samples[0], return_std=True)
    cdf_all = []
    print(y_pred)
    for i in range(len(y_pred)):
        a = stats.norm(y_pred[i], sigma_st[i]).cdf(0)
        print(a)
        cdf_all.append(a)
    print(np.array(cdf_all).shape)

    f = ax.scatter(samples[0][:,0],samples[0][:,1],samples[0][:,2],c = cdf_all, cmap="RdYlBu")
    plt.colorbar(f, ax = ax)
    plt.savefig(im_dir, dpi = 400)

BENCHMARK_NAME = "f16_alt2300_budget_5000"

result_directory = pathlib.Path().joinpath('result_files_final_alpha').joinpath(BENCHMARK_NAME).joinpath(BENCHMARK_NAME + "_result_generating_files")

f = open(result_directory.joinpath(BENCHMARK_NAME + "_options.pkl"), "rb")
options = pickle.load(f)
f.close()

# f = open(result_directory.joinpath(BENCHMARK_NAME + "_mc_truefv_test_function.pkl"), "rb")
# mc_uniform_test_function = pickle.load(f)
# f.close()
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# f = ax.scatter(mc_uniform_test_function['x'][0,:,0],mc_uniform_test_function['x'][0,:,1],mc_uniform_test_function['x'][0,:,2],c = mc_uniform_test_function['y'][0,:], cmap="RdYlBu")
# ticks = np.linspace(mc_uniform_test_function['y'][0,:].min(), mc_uniform_test_function['y'][0,:].max(), 10, endpoint=True)
# cbar = plt.colorbar(f, ax = ax, ticks = ticks)
# # cbar.set_
# plt.show()

# print(mc_uniform_test_function)
# for i in range(50):
#     tree_dir = result_directory.joinpath(BENCHMARK_NAME + "_" + str(i)+".pkl")
#     im_dir = result_directory.joinpath(BENCHMARK_NAME + "_" + str(i)+"_regions.svg")
#     save_trees_plots(i, tree_dir, im_dir, options)

# result_directory = pathlib.Path().joinpath('result_files').joinpath(BENCHMARK_NAME).joinpath(BENCHMARK_NAME + "_result_generating_files")
    
start_seed = 1000
for i in range(1):
    im_dir = result_directory.joinpath(BENCHMARK_NAME + "_" + str(i)+"_scatter.png")
    rng = np.random.default_rng(start_seed+i)
    tree_dir = result_directory.joinpath(BENCHMARK_NAME + "_" + str(i)+".pkl")
    # values_dir = result_directory.joinpath(BENCHMARK_NAME + "_" + str(i)+"_scatter.png")

    f = open(result_directory.joinpath(BENCHMARK_NAME + "_" + str(i) + "_point_history.pkl"), "rb")
    point_history = pickle.load(f)
    f.close()
        
    point_history = np.array(point_history)
    # import pandas as pd
    # X_ = point_history[:,1]
    # X = np.array([X_[i].tolist() for i in range(len(X_))])
    # Y = np.transpose(point_history[:,-1])
    # print(Y.max())
    # print(Y.min())
    # Y = np.transpose(Y_)
    
    # generate_scatterplot(8000, i, im_dir, options, model, rng)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    f = open(tree_dir, "rb")
    ftree = pickle.load(f)
    f.close()

    leaves = ftree.leaves()
    print(len(leaves))
    # plt.show()
    s_1 = []
    s_2 = []
    s_3 = []
    y = []
    for i in leaves:
        
        X = i.data.samples_in[0]
        Y = np.transpose(i.data.samples_out)
        model = GaussianProcessRegressor()
        model.fit(X, Y)

        samples = i.data.grid[0,:,:]
        y_pred, sigma_st = model.predict(samples, return_std=True)
        cdf_all = []
        # print(y_pred)
        for i in range(len(y_pred)):
            
            a = stats.norm.cdf(0.0, y_pred[i][0], sigma_st[i])
            print("{}, {} -> {}".format(y_pred[i][0], sigma_st[i], a))
            # print(a)
            y.append(a)
        # print(np.array(cdf_all).shape)
        s_1.extend(samples[:,0])
        s_2.extend(samples[:,1])
        s_3.extend(samples[:,2])
        print(np.array(s_1).shape)
    f = ax.scatter(s_1, s_2, s_3,c = y, cmap="RdYlBu")
    # plt.colorbar(f, ax = ax)
    plt.show()
