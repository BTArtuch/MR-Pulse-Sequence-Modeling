from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT_DIR / "output"

def discrete_t1_decay(T1, t):
    '''
        Discrete test function to observe the behavior of the decay function
         at T1 (s) over 1 second increments t (90 degree pulse)
    '''
    for i in range(1,t+1):
        M0 = 1 # Just normalize the magnetization vector for demonstration
        Mz_t = M0 * (1 - np.exp(-i/T1)) # 90 degree B1 pulse decay
        print(Mz_t)

def continuous_t1_decay_plot(T1, t):
    '''
        Continuous visualization of the T1 (s) decay for a single tissue over
         time t (s) (90 degree pulse)
    '''
    t = np.linspace(0.0,float(t), 201)
    M0 = 1.0 # Just normalize the magnetization vector for demonstration
    Mz_t = M0 * (1.0 - np.exp(-t/T1)) # 90 degree B1 pulse decay

    fig, ax = plt.subplots()
    ax.plot(t, Mz_t)

    output_path = OUTPUT_DIR / "t1_fat_relaxation.png"
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved figure to: {output_path}")

def t1_multi_plot(T1_list, t):
    '''
        Continuous visualization of the T1 (s) decays for a list of multiple tissues over
         time t (s) (90 degree pulse)
    '''
    t = np.linspace(0.0,float(t), 201)
    M0 = 1.0 # Just normalize the magnetization vector for demonstration
    
    Mz_list = []

    for T1_value in T1_list:
        Mz_t = M0 * (1.0 - np.exp(-t/T1_value)) # 90 degree B1 pulse decay
        Mz_list.append(Mz_t)

    fig, ax = plt.subplots()

    for i in range(0,len(Mz_list)):
        ax.plot(t, Mz_list[i])

    output_path = OUTPUT_DIR / "t1_multi_relaxation.png"
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved figure to: {output_path}")
