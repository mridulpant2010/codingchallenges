import os
import sys
from collections import Counter

current_dir = os.path.dirname(__file__)
parent_dir= os.path.dirname(current_dir)
sys.path.append(parent_dir)
print(parent_dir)
from src.main import build_heap


def main():
    text_str = """
    There has been perennial interest in personal qualities other than cognitive ability that determine success, including self-
    control, grit, growth mind-set, and many others. Attempts to measure such qualities for the purposes of educational
    policy and practice, however, are more recent. In this article, we identify serious challenges to doing so. We first address
    confusion over terminology, including the descriptor noncognitive. We conclude that debate over the optimal name for
    this broad category of personal qualities obscures substantial agreement about the specific attributes worth measuring.
    Next, we discuss advantages and limitations of different measures. In particular, we compare self-report questionnaires,
    teacher-report questionnaires, and performance tasks, using self-control as an illustrative case study to make the general
    point that each approach is imperfect in its own way. Finally, we discuss how each measure’s imperfections can affect its
    suitability for program evaluation, accountability, individual diagnosis, and practice improvement. For example, we do
    not believe any available measure is suitable for between-school accountability judgments. In addition to urging caution
    among policymakers and practitioners, we highlight medium-term innovations that may make measures of these personal
    qualities more suitable for educational purposes
    """
    frequency_map = Counter(text_str)
    print(frequency_map.items())
    
    result = build_heap(frequency_map)
    print(result)
    
if __name__ == "__main__":
    main()
