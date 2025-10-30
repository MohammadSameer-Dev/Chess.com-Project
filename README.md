# Chess.com-Project

> A set of Python scripts and helpers to capture, extract and analyze chess boards from screenshots (initial work-in-progress).

---

## Project status

This repository contains early-stage tooling for capturing a chessboard from a screen/image, splitting it into square images and performing basic board analysis. Development is currently paused but the code is usable and meant to be a foundation for further work.

---

## Features

* `capture_board.py` — helpers to take or load a screenshot of a chessboard (desktop / saved image).
* `extract_squares.py` — split a detected board into 64 square images for downstream recognition.
* `analyze_board.py` — basic analysis routines (placeholder for piece recognition, FEN generation, engine evaluation).
* `stockfish/` — (included) example engine integration to evaluate positions.
* `board_squares/`, `templates/` — supporting data and templates used by the scripts.

---

## Repository layout

```
Chess.com-Project/
├─ .vscode/
├─ board_squares/        # output / test square images
├─ stockfish/            # engine binaries or wrappers (check platform compatibility)
├─ templates/            # any template images used for detection / matching
├─ analyze_board.py
├─ capture_board.py
├─ extract_squares.py
├─ board_capture.png      # example screenshot
├─ README.md
└─ LICENSE (Apache-2.0)
```

---

## Getting started

> These are suggested steps to run the current scripts locally. The repo does not yet include a `requirements.txt`; add one when you pin dependency versions.

### Prerequisites

* Python 3.8+ (3.10 recommended)
* Basic image / computer-vision libraries

Suggested Python packages (install with `pip`):

```bash
pip install opencv-python numpy pillow matplotlib
# Optional (for OCR/advanced recognition):
pip install pytesseract
# If you integrate Stockfish via pip wrappers:
pip install stockfish
```

You'll also need the Stockfish engine binary for your platform if you plan to run engine evaluations. Place it under the `stockfish/` folder or point your code to the binary path.

### Run the scripts

1. Capture or provide a board image:

```bash
python capture_board.py --input path/to/board_screenshot.png
```

2. Extract squares:

```bash
python extract_squares.py --input path/to/board_screenshot.png --out-folder board_squares/
```

3. Analyze board (generate FEN / evaluate):

```bash
python analyze_board.py --input path/to/board_screenshot.png
```

> The exact CLI arguments may change; open the top of each script to see the current parameter names and usage examples.

---

## How it works (high level)

1. **Board detection** — locate the chessboard inside a screenshot using contour detection, template matching or Hough transforms.
2. **Board normalization** — warp-perspective the board to obtain a square, axis-aligned view.
3. **Square extraction** — split the normalized board into an 8×8 grid and save each cell as an image.
4. **Piece recognition & FEN** — apply a piece recognizer (template matching / classifier / OCR) to produce a FEN string.
5. **Engine evaluation** — feed the FEN to Stockfish for evaluation / best-move suggestions.

This repo currently implements steps 1–3 and scaffolds for step 4–5.

---

## Improvements & TODO

* Add a `requirements.txt` and pin versions.
* Improve board detection robustness (lighting, board themes on Chess.com).
* Replace naive template matching with a trained classifier (CNN) for piece recognition.
* Add unit tests and CI (GitHub Actions).
* Provide cross-platform Stockfish download/installation instructions.
* Add example images / dataset and a small demo notebook.

---

## Contribution guide

Contributions, issues and suggestions are welcome. If you want to help:

* Open an issue describing what you want to add or improve.
* Fork the repo and create a feature branch.
* Keep changes focused and add documentation / examples for new functionality.

When submitting a PR, include:

* A short description of the change.
* How to run / test it locally.

---

## License

This repository is licensed under the **Apache-2.0** License. See the `LICENSE` file for details.

---

## Credits & resources

* Built by MohammadSameer-Dev — experimental project.
* Recommend reading on board detection and chess FEN:

  * OpenCV documentation — image transforms & contour detection
  * Stockfish project — engine integration

---


