import pathlib
import pickle
from partx.models.partx_options import partx_options
from partx.executables.generate_statistics import generate_statistics
import matplotlib.pyplot as plt
import numpy as np

BENCHMARK_NAME = "f16_alt2300_budget_2"
result_directory = pathlib.Path().joinpath('f16_final_results_UR_replications').joinpath(BENCHMARK_NAME).joinpath(BENCHMARK_NAME + "_result_generating_files")
num_macro_rep = 50
for rep_number in range(num_macro_rep):
    f = open(result_directory.joinpath(BENCHMARK_NAME + "_" + str(rep_number) +"_uniform_random_results.pkl"), "rb")
    result_dictionary = pickle.load(f)
    f.close()
    samples_in =  result_dictionary["samples"][0]
    robustness = result_dictionary["robustness"][0]
    print(samples_in)
    print(robustness)
    print("**************")
# print(np.sum(robustness<0))
# print(samples_in.shape)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# f = ax.scatter(samples_in[:,0], samples_in[:,1], samples_in[:,2], c = robustness, cmap="RdYlBu")
# ticks = np.linspace(robustness.min(), robustness.max(), 10, endpoint=True)
# cbar = plt.colorbar(f, ax = ax, ticks = ticks)
# plt.show()

# number_of_macro_replications = 50
# quantiles_at = [0.5, 0.95, 0.99]
# confidence_at = 0.95
# # start_seed = 5000
# result_dictionary = generate_statistics(BENCHMARK_NAME, number_of_macro_replications, quantiles_at, confidence_at,'f16_final_results')




# for key, value in result_dictionary.items():
#     print("{} : {}".format(key, value))

# # print("{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}".format(result_dictionary['true_fv'],
# #                 result_dictionary['mean_fv_with_gp_quan0_5'],
# #                 result_dictionary['std_dev_fv_with_gp_quan0_5'],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][0],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][1],
# #                 result_dictionary['mean_fv_with_gp_quan0_95'],
# #                 result_dictionary['std_dev_fv_with_gp_quan0_95'],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][0],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][1],
# #                 result_dictionary['mean_fv_with_gp_quan0_99'],
# #                 result_dictionary['std_dev_fv_with_gp_quan0_99'],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][0],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][1],
# #                 result_dictionary['mean_fv_wo_gp_classified'],
# #                 result_dictionary['std_dev_fv_wo_gp_classified'],
# #                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][0],
# #                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][1],
# #                 result_dictionary['mean_fv_wo_gp_classified_unclassified'],
# #                 result_dictionary['std_dev_fv_wo_gp_classified_unclassified'],
# #                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][0],
# #                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][1],))

# print("********************")
# print("{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}".format(result_dictionary['true_fv'],
#                 result_dictionary['falsification_rate'],
#                 result_dictionary['numpoints_fin_first_f_min'],
#                 result_dictionary['numpoints_fin_first_f_max'],
#                 result_dictionary['numpoints_fin_first_f_mean'],
#                 result_dictionary['numpoints_fin_first_f_median'],
#                 result_dictionary['mean_fv_with_gp_quan0_5'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_5'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][1],
#                 result_dictionary['mean_fv_with_gp_quan0_95'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_95'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][1],
#                 result_dictionary['mean_fv_with_gp_quan0_99'],
#                 result_dictionary['std_dev_fv_with_gp_quan0_99'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][1],
#                 result_dictionary['best_robustness']
#                 ))

# # print("{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}".format(result_dictionary['true_fv'],
# #                 result_dictionary['mean_fv_with_gp_quan0_5'],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][0],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][1],
# #                 result_dictionary['mean_fv_with_gp_quan0_95'],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][0],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][1],
# #                 result_dictionary['mean_fv_with_gp_quan0_99'],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][0],
# #                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][1],
# #                 result_dictionary['mean_fv_wo_gp_classified'],
# #                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][0],
# #                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][1],
# #                 result_dictionary['mean_fv_wo_gp_classified_unclassified'],
# #                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][0],
# #                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][1]))