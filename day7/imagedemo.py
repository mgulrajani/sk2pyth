from pathlib import Path

p1=Path('images/images2')

for name in p1.glob('*.g*'):
    print(name)
