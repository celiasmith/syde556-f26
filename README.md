# Course material for SYDE 556/750

Course website: http://compneuro.uwaterloo.ca/courses/syde-750.html

Fall 2026 — classes run Sep 9 to Dec 8. Tuesdays 12:00–1:50 and Thursdays
12:00–12:50, in E5 2004. There are no classes during reading week (Oct 13
and Oct 15). 

## 🎒 Lectures

Slides and notes will be linked here as the term progresses.

- Sep 10 - Administrative Remarks [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_00/syde556_lecture_00_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_00/syde556_lecture_00_notes.pdf)-->]
- Sep 10 - Introduction [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_01/syde556_lecture_01_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_01/syde556_lecture_01_notes.pdf)-->]
- Sep 15 - Neurons [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_02/syde556_lecture_02_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_02/syde556_lecture_02_notes.pdf)-->]
- Sep 17, 22 - Population Representation [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_03/syde556_lecture_03_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_03/syde556_lecture_03_notes.pdf)-->]
- Sep 24, 29 - Temporal Representation [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_04/syde556_lecture_04_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_04/syde556_lecture_04_notes.pdf)-->]
- Oct 1, 6 - Feedforward Transformations [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_05/syde556_lecture_05_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_05/syde556_lecture_05_notes.pdf)-->]
- Oct 8 - Nengo Tutorial [[Install Nengo](https://www.nengo.ai/getting-started/)]
- Oct 20, 22 - Recurrent Dynamics [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_06/syde556_lecture_06_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_06/syde556_lecture_06_notes.pdf)-->]
- Oct 27 - Temporal Basis Functions [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_07/syde556_lecture_07_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_07/syde556_lecture_07_notes.pdf)-->] [[LMU Overview]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_07/LMU%20Overview%20for%20SYDE%20556.pdf)-->]
- Oct 29, Nov 3, 5 - Learning [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_08/syde556_lecture_08_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_08/syde556_lecture_08_notes.pdf)-->] [[Neuromorphics Bonus]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_05/neuromorphics_intro_2022.pdf)-->] [[Adaptive Control Example]<!--(https://github.com/tcstewar/nengo_learning_examples/blob/master/control/pendulum_pd_adaptive.py)-->] (project proposal due Oct 29)
- Nov 10 - Analysing Representation [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_09/syde556_lecture_09_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_09/syde556_lecture_09_notes.pdf)-->]
- Nov 12, 17 - Symbols [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_10/syde556_lecture_10_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_10/syde556_lecture_10_notes.pdf)-->]
- Nov 19, 24 - Semantic Pointer Architecture [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_11/syde556_lecture_11_slides_distr.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_11/syde556_lecture_11_notes.pdf)-->]
- Nov 26, Dec 1 - Spatial Semantic Pointers [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_14/syde556_lecture_14_slides.pdf)-->] [[Notes]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_14/syde556_lecture_14_notes.pdf)-->]
- Dec 3 - Conclusion [[Slides]<!--(https://github.com/celiasmith/syde556-f26/raw/master/lectures/lecture_13/syde556_lecture_13_slides.pdf)-->]
- Dec 8 - Project Presentations
- Dec 18 - Projects due (midnight ET)

## 📓 Practice Notebooks

There are no graded programming assignments in this course. Instead, six
ungraded practice notebooks (PN1–PN6) will be posted here over the term.

- Each notebook covers the material for the test that follows it, and one or
  two questions on each test come directly from the matching notebook.
- No solutions are released. Instead, each part ends with a qualitative
  expected-result checkpoint so you can verify your work yourself.
- You are expected to work through the notebooks individually.

The notebooks require `nengo`, `nengo_spa`, `numpy`, `matplotlib`, and
`scipy`. PN1 and PN2 are pure `numpy`, so you hand-code decoders yourself;
PN3 onward uses Nengo.

- PN1 - Neurons and Population Representation [[Notebook](https://github.com/celiasmith/syde556-f26/raw/master/practice_notebooks/556_PN1_neurons_and_population.ipynb)]
- PN2 - Temporal Representation and Transformations [[Notebook]<!--(https://github.com/celiasmith/syde556-f26/raw/master/practice_notebooks/556_PN2_temporal_and_transformations.ipynb)-->]
- PN3 - Nengo and Simple Dynamics [[Notebook]<!--(https://github.com/celiasmith/syde556-f26/raw/master/practice_notebooks/556_PN3_nengo_and_simple_dynamics.ipynb)-->]
- PN4 - Decision Making, Learning, and the LMU [[Notebook]<!--(https://github.com/celiasmith/syde556-f26/raw/master/practice_notebooks/556_PN4_decision_learning_and_lmu.ipynb)-->]
- PN5 - Symbols and the Semantic Pointer Architecture [[Notebook]<!--(https://github.com/celiasmith/syde556-f26/raw/master/practice_notebooks/556_PN5_symbols_and_spa.ipynb)-->]
- PN6 - Spatial Semantic Pointers [[Notebook]<!--(https://github.com/celiasmith/syde556-f26/raw/master/practice_notebooks/556_PN6_spatial_semantic_pointers.ipynb)-->]

## 📝 Tests

There are six closed-book tests, written in class during the
last 30 minutes of a Thursday lecture, roughly every two weeks. The lowest
of the six marks is dropped.

| Notebook | Posted | Test | Test date |
|---|---|---|---|
| [PN1](https://github.com/celiasmith/syde556-f26/raw/master/practice_notebooks/556_PN1_neurons_and_population.ipynb) | Sep 10 | T1 | Sep 24 |
| PN2 | Sep 22 | T2 | Oct 8 |
| PN3 | Oct 6 | T3 | Oct 29 |
| PN4 | Oct 27 | T4 | Nov 12 |
| PN5 | Nov 10 | T5 | Nov 26 |
| PN6 | Nov 24 | T6 | Dec 3 |
