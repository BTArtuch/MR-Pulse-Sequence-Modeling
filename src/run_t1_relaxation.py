from include.t1_relaxation_math import continuous_t1_decay_plot, t1_multi_plot

if __name__ == "__main__":
    t1 = 0.4 # (seconds)
    t = 6.0 # (seconds)
    # continuous_t1_decay_plot(t1,t)

    t1_dict = {"Fat" : 0.4, "Muscle" : 1.6, "CSF" : 3.2 } # [fat, muscle, CSF (Cerebrospinal Fluid)]
    t1_multi_plot(t1_dict, t)
