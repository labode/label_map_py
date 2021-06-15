# Label Colormap Generator
Small tool to generate a list of 1331 (=11³) equally spaced colors.
List is shuffled, as to have a high degree of dissimilarity between neighboring colors.
First color is always [0, 0, 0].
The program will output a .png of the colors, and a .csv containing the color codes to be used in another program.

## Input
- filename to write output to (will be used both for .csv and .png)

## Output
- .csv containing coma separated RGB colors, one per line
- .png rendering of the color map

## Usage
### Example
`python3 main.py output`