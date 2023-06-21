# (de)Motivational Poster Generator
A program written in Python to automatically generate both motivational and demotivational posters.

## Setup
Install requirements with `pip install -r requirements.txt`

## Usage
```
python makeposter.py [-h] [-p PROMPT] [-d]

options:
  -h, --help            show this help message and exit
  -p PROMPT, --prompt PROMPT
                        the main word for the poster
  -d, --demotivate      makes a demotivational instead of a motivational
```
## Examples

### Motivational
`python makeposter.py -p github`

![github](https://github.com/DPS2004/motivationalposters/assets/10176105/161a4d8a-3d4b-4d0e-93bc-096c6c929fe7)

`python makeposter.py -p sandbox`

![sandbox](https://github.com/DPS2004/motivationalposters/assets/10176105/37fca100-3620-4ca2-96b4-4845b29e38e3)

`python makeposter.py -p "boxing gloves"`

![boxing gloves](https://github.com/DPS2004/motivationalposters/assets/10176105/98da107f-d0ed-45ad-a418-8890d5133b69)
### Demotivational
`python makeposter.py -d -p lightbulb`

![lightbulb](https://github.com/DPS2004/motivationalposters/assets/10176105/4c155520-1727-437a-8406-02040be01a49)

`python makeposter.py -d -p python`

![python](https://github.com/DPS2004/motivationalposters/assets/10176105/ab060d8d-17f6-4fd7-8444-3190cfd6923e)

`python makeposter.py -d -p "washing machine"`

![washing machine](https://github.com/DPS2004/motivationalposters/assets/10176105/8261beab-f772-40d3-b909-e64ad97d2562)
