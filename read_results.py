import pathlib
import pickle
from partx.models.partx_options import partx_options
from partx.executables.generate_statistics import generate_statistics
import matplotlib.pyplot as plt
import numpy as np
# from read_UR_results import read_UR_results
import logging
from partx.executables.exp_statistics import falsification_volume_using_gp
# BENCHMARK_NAMES = ["f16_alt2300_budget_5000",
#                    "f16_alt2330_budget_5000",
#                    "f16_alt2338_budget_5000",
#                    "f16_alt2338_2_budget_5000",
#                    "f16_alt2338_4_budget_5000",
#                    "f16_alt2338_5_budget_5000",
#                    "f16_alt2338_6_budget_5000",
#                    "f16_alt2350_budget_5000",
                #    "f16_alt2400_budget_5000"]

BENCHMARK_NAMES = ["f16_alt2300_budget_5000"]

log = logging.getLogger()
log.setLevel(logging.INFO) 
fh = logging.FileHandler(filename = pathlib.Path().joinpath("f16_result_logs.log"))
formatter = logging.Formatter(
                fmt = '%(message)s'
                )

fh.setFormatter(formatter)
log.addHandler(fh)

for BENCHMARK_NAME in BENCHMARK_NAMES:                    
    result_directory = pathlib.Path().joinpath('f16_final_results_1').joinpath(BENCHMARK_NAME).joinpath(BENCHMARK_NAME + "_result_generating_files")

    f = open(result_directory.joinpath(BENCHMARK_NAME + "_options.pkl"), "rb")
    options = pickle.load(f)
    f.close()

    number_of_macro_replications = 50
    quantiles_at = [0.5, 0.95, 0.99]
    confidence_at = 0.95
    result_dictionary = generate_statistics(BENCHMARK_NAME, number_of_macro_replications, quantiles_at, confidence_at,'f16_final_results')

    print("**************************")
    print(result_dictionary)
    print("**************************")

    # for i in range(number_of_macro_replications):
    #     f = open(result_directory.joinpath(BENCHMARK_NAME+ "_" + str(i) + ".pkl"), "rb")
    #     ftree = pickle.load(f)
    #     f.close()

    #     falsification_volume_using_gp(ftree, options, quantiles_at, rng)

    # for key, value in result_dictionary.items():
    #     print("{} : {}".format(key, value))

    
    
    # FR, mean_fv, std_error_fv, con_int_0, con_int_1, best_rob = read_UR_results(BENCHMARK_NAME, confidence_at, number_of_macro_replications)

    log.info("{};{};{};{};{};{}".format(result_dictionary['falsification_rate'],
                                result_dictionary['mean_fv_with_gp_quan0_99'],
                                result_dictionary['std_dev_fv_with_gp_quan0_99'],
                                result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][0],
                                result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][1],
                                result_dictionary['best_robustness']))
    # log.info("{};{};{};{};{};{}".format(FR, mean_fv, std_error_fv, con_int_0, con_int_1, best_rob))

# print("{};{};{};{};{};{}".format(result_dictionary['falsification_rate'],
#                             result_dictionary['mean_fv_with_gp_quan0_95'],
#                             result_dictionary['std_dev_fv_with_gp_quan0_95'],
#                             result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][0],
#                             result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][1],
#                             result_dictionary['best_robustness']))

# print("{};{};{};{};{};{}".format(result_dictionary['falsification_rate'],
#                             result_dictionary['mean_fv_with_gp_quan0_99'],
#                             result_dictionary['std_dev_fv_with_gp_quan0_99'],
#                             result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][0],
#                             result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][1],
#                             result_dictionary['best_robustness']))

# print("{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}".format(result_dictionary['true_fv'],
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
#                 result_dictionary['mean_fv_wo_gp_classified'],
#                 result_dictionary['std_dev_fv_wo_gp_classified'],
#                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][1],
#                 result_dictionary['mean_fv_wo_gp_classified_unclassified'],
#                 result_dictionary['std_dev_fv_wo_gp_classified_unclassified'],
#                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][1],))

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

# print("{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}".format(result_dictionary['true_fv'],
#                 result_dictionary['mean_fv_with_gp_quan0_5'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_5_confidence_0_95'][1],
#                 result_dictionary['mean_fv_with_gp_quan0_95'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_95_confidence_0_95'][1],
#                 result_dictionary['mean_fv_with_gp_quan0_99'],
#                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_with_gp_quan_0_99_confidence_0_95'][1],
#                 result_dictionary['mean_fv_wo_gp_classified'],
#                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_wo_gp_classified_quan_confidence_0_95'][1],
#                 result_dictionary['mean_fv_wo_gp_classified_unclassified'],
#                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][0],
#                 result_dictionary['con_int_fv_wo_gp_classified_unclassified_quan_confidence_0_95'][1]))