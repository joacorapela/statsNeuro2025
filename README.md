# Neuroinformatics for SWC PhD students 2025 repository

- material related to lectures can be found [here](https://github.com/joacorapela/neuroinformatics25/tree/master/lectures)

- material related to discussion sessions can be found [here](https://github.com/joacorapela/neuroinformatics25/tree/master/practicals)

- worksheets can be found [here](https://github.com/joacorapela/neuroinformatics25/tree/master/worksheets)

- <a name="lecturesSchedule"></a>lectures schedule:

    <table>
    <tr>
        <th>Week</th>
        <th>Date</th>
        <th>Topic</th>
        <th>Lecturers</th>
        <th>Type</th>
    </tr>
    <tr>
        <td>01</td>
        <td>Jan 15</td>
        <td>Intro to stats, hypothesis testing</td>
        <td><a href="https://www.gatsby.ucl.ac.uk/">Joaquin Rapela</a></td>
        <td>lecture</td>
    </tr>
    <tr>
        <td bgcolor="blue" colspan="5">This content spans five columns</td>
    </tr>
    </table>

    | Week | Date  | Topic | Lecturers | Type |
    |------|-------|-------|-----------|------|
    | 01 | Jan 15 | Intro to stats, hypothesis testing | [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/) | lecture |
    | 01 | Jan 16 | [The t-test and randomization test](https://github.com/joacorapela/neuroinformatics24/blob/master/practicals/01_tTestAndRandomizationTests/introAndHipothesisTests.pdf) | [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/~rapela) | practical |
    | 02 | Jan 22 | Spectral analysis of stationary signals | [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/) | lecture |
    | 02 | Jan 23 | [Power spectra](https://github.com/joacorapela/neuroinformatics24/blob/master/practicals/02_LFPs_spectralAnalysis/spectralAnalysis.pdf) | [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/~rapela) | practical |
    | 03 | Jan 29 | Spectral analysis of non-stationary signals, multiple time series | [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/) | lecture |
    | 03 | Jan 30 | [Spectrogram and coherence](https://github.com/joacorapela/neuroinformatics24/blob/master/practicals/03_spectralAnalysisForNonStationarySignals/nonStationarySpectralAnalysis.pdf) | [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/~rapela) | practical |
    | 04 | Feb 05 | Dimensionality reduction | [Will Dorrell](https://www.williamdorrell.co.uk/) | lecture |
    | 04 | Feb 06 | Dimensionality Reduction | [Will Dorrell](https://www.williamdorrell.co.uk/)| practical |
    | 05 | Feb 12 | Clustering | | lecture |
    | 05 | Feb 13 | Clustering | | practical |
    | 06 | Feb 19 | Linear Dynamical Systems, Hidden Markov Models | | lecture |
    | 06 | Feb 20 | [Linear Dynamical Systems](https://github.com/joacorapela/neuroinformatics24/blob/master/practicals/06_linearDynamicalSystems/README.md) | | practical |
    | 07 | Feb 26 | Spike Sorting | | lecture |
    | 07 | Feb 27 | Spike sorting | | practical |
    | 08 | Feb 05 | [Linear Regression](https://github.com/joacorapela/neuroinformatics24/blob/master/lectures/06_linearRegression/swc_neuroinformatics_linreg.pdf) | [Lior Fox](https://liorfox.github.io/) | lecture |
    | 08 | Feb 06 | Linear Regression | [Lior Fox](https://liorfox.github.io/) | practical |
    | 09 | Mar 12 | [Artificial Neural Networks](https://slides.com/eringrant/2024-03-07-swc-neural-nets-lecture/fullscreen?token=Gq60IrMy) | [Erin Grant](https://eringrant.github.io/) | lecture |
    | 09 | Mar 13 | Artificial Neural Networks | [Erin Grant](https://eringrant.github.io/) | practical |
    | 10 | Mar 19 | [Reinforcement learning](lectures/10_reinforcementLearning/RLinTheBrain_SWC_2024.pdf) | [Jesse Geerts](https://scholar.google.com/citations?user=4xusDVAAAAAJ&hl=en) | lecture |
    | 10 | Mar 20 | Reinforcement learning | [Jesse Geerts](https://scholar.google.com/citations?user=4xusDVAAAAAJ&hl=en) | practical |
    | 11 | Mar 26 | [Experimental Control with Bonsai](https://neurogears.org/neuroinformatics-2024/) | [Goncalo Lopez](https://neurogears.org/about-us/) [Nick Guilbeault](https://www.linkedin.com/in/ncguilbeault/) | lecture |
    | 11 | Mar 27 | Experimental Control with Bonsai | [Goncalo Lopez](https://neurogears.org/about-us/) [Nick Guilbeault](https://www.linkedin.com/in/ncguilbeault/) [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/~rapela) | practical |

- running scripts: we recommend that you run the provided scripts in a conda environment. Before running any script do (only once):

    1. `conda create -n neuroi python`
    2. clone this repository (`git clone git@github.com:joacorapela/neuroinformatics25.git`)

    3. change to the repository directory (`cd neuroinformatics25`)
    4. activate your conda environment (`conda activate neuroi`)
    5. type `pip install -r requirements.txt`

    Then you can run any script by (for example):

    - `cd practicals/02_LFPs_spectralAnalysis/exercises/`
    - `python doReconstructionExercise.py`

- If you have any problem running scripts in this repo, please contact [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/~rapela).

