# Neuroinformatics for SWC PhD students 2025 repository

- material related to lectures can be found [here](https://github.com/joacorapela/neuroinformatics25/tree/master/lectures)

- material related to discussion sessions can be found [here](https://github.com/joacorapela/neuroinformatics25/tree/master/practicals)

- worksheets can be found [here](https://github.com/joacorapela/neuroinformatics25/tree/master/worksheets)

- <a name="lecturesSchedule"></a>lectures schedule:

    | Week | Date  | Topic | Lecturers | Type |
    |------|-------|-------|-----------|------|
    | 01 | Jan 15 | [Review of statistics](https://drive.google.com/open?id=1okjYVeDQZ4-lqliY7qD9rmBg7Tbc1kwE) [Spike Trains](https://drive.google.com/open?id=1hFg6F79iodNyaPuKxqNTf8cVlbY9X_z-)| [Ken Harris](https://www.ucl.ac.uk/biosciences/people/harris-kenneth) | lecture |
    | 01 | Jan 16 | [The t-test and randomization tests](https://github.com/joacorapela/neuroinformatics24/blob/master/practicals/01_tTestAndRandomizationTests/introAndHipothesisTests.pdf) | [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/~rapela) | practical |
    | 02 | Jan 22 | [LFPs](https://drive.google.com/open?id=1qi1rdHUP3atLSMbcVeOfJkmJdV7jRyuD) [Spectral analysis](https://drive.google.com/open?id=1RV8X-vJ-Zpiv867_5D6TpbzcP-Ob9IlB)| [Ken Harris](https://www.ucl.ac.uk/biosciences/people/harris-kenneth) | lecture |
    | 02 | Jan 23 | [Power spectra](https://github.com/joacorapela/neuroinformatics24/blob/master/practicals/02_LFPs_spectralAnalysis/spectralAnalysis.pdf) | [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/~rapela) | practical |
    | 03 | Jan 29 | [Spectrogram and non-stationary signals](https://drive.google.com/open?id=1j0m136j8Gks9L2vzja33S675KLShnN3P) [Multiple time series](https://drive.google.com/open?id=10drGN8gBTX86u7jkW55b4BE7i8g6nmN_) | [Ken Harris](https://www.ucl.ac.uk/biosciences/people/harris-kenneth) | lecture |
    | 03 | Jan 30 | [Spectrogram and coherence](https://github.com/joacorapela/neuroinformatics24/blob/master/practicals/03_spectralAnalysisForNonStationarySignals/nonStationarySpectralAnalysis.pdf) | [Joaquin Rapela](https://www.gatsby.ucl.ac.uk/~rapela) | practical |
    | 04 | Feb 05 | [Circular statistics and local likelihood](https://drive.google.com/open?id=1_fkUwIpcu-s8D8D_DL53_MRuDQjI9RDa) [The bootstrap](https://drive.google.com/open?id=1GrL--CypH_Bjr5MuVXSda8r_CzfQdLCA) | [Ken Harris](https://www.ucl.ac.uk/biosciences/people/harris-kenneth) | lecture |
    | 04 | Feb 06 | [Circular statistics](https://github.com/joacorapela/neuroinformatics24/blob/master/practicals/04_circulaVariables_bootstrap) | | practical |
    | 05 | Feb 12 | [Singular Value Decomposition](https://drive.google.com/open?id=10dBiM36EMYxg5m0EqhnArj3KUk3AIElT) [Dimensionality reduction](https://drive.google.com/open?id=1sVtWgqx4yylPJrlIB3DdeluzQRhU2GDi) | [Ken Harris](https://www.ucl.ac.uk/biosciences/people/harris-kenneth) | lecture |
    | 05 | Feb 13 | [Singular Value Decomposition](practicals/05_singularValueDecomposition/singularValueDecomposition.pdf) | | practical |
    | 06 | Feb 19 | [Linear Regression](https://github.com/joacorapela/neuroinformatics24/blob/master/lectures/06_linearRegression/swc_neuroinformatics_linreg.pdf) | [Lior Fox](https://liorfox.github.io/) | lecture |
    | 06 | Feb 20 | Linear Regression | [Lior Fox](https://liorfox.github.io/) | practical |
    | 07 | Feb 26 | [Linear Dynamical Systems](https://github.com/joacorapela/neuroinformatics24/blob/master/lectures/07_linearDynamicalSystems) | | lecture |
    | 07 | Feb 27 | [Linear Dynamical Systems](https://github.com/joacorapela/neuroinformatics24/blob/master/practicals/06_linearDynamicalSystems/README.md) | | practical |
    | 08 | Mar 05 | [Artificial Neural Networks](https://slides.com/eringrant/2024-03-07-swc-neural-nets-lecture/fullscreen?token=Gq60IrMy) | [Erin Grant](https://eringrant.github.io/) | lecture |
    | 08 | Mar 06 | Artificial Neural Networks | [Erin Grant](https://eringrant.github.io/) | practical |
    | 09 | Mar 12 | [Reinforcement learning](lectures/10_reinforcementLearning/RLinTheBrain_SWC_2024.pdf) | [Jesse Geerts](https://scholar.google.com/citations?user=4xusDVAAAAAJ&hl=en) | lecture |
    | 10 | Mar 13 | Reinforcement learning | [Jesse Geerts](https://scholar.google.com/citations?user=4xusDVAAAAAJ&hl=en) | practical |
    | 09 | Mar 19 | [Experimental Control with Bonsai](https://neurogears.org/neuroinformatics-2024/) | [Goncalo Lopez](https://neurogears.org/about-us/) [Nick Guilbeault](https://www.linkedin.com/in/ncguilbeault/) | lecture |
    | 10 | Mar 20 | Experimental Control with Bonsai | [Goncalo Lopez](https://neurogears.org/about-us/) [Nick Guilbeault](https://www.linkedin.com/in/ncguilbeault/) | practical |

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

