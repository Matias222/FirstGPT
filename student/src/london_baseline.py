# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0

    predicciones=[]

    with open("C:\\Users\\matia\\Desktop\\224N\\a4_spr24_student_code\\student\\vanilla.nopretrain.dev.predictions", "r", encoding="utf-8") as f:
        a=f.read().split("\n")
        for i in a: predicciones.append(i)

    predicciones=["London"]*500

    total,correctas=utils.evaluate_places("C:\\Users\\matia\\Desktop\\224N\\a4_spr24_student_code\\student\\birth_dev.tsv",predicciones)

    print(correctas,total)

    accuracy=correctas/total

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
