# main.py

from scheduler import generate_timetables
import json

def load_courses(path):
    """
    JSON 파일에서 과목 정보를 불러오는 함수
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    # data 폴더에서 예시 과목 불러오기
    courses = load_courses("data/sample_input.json")

    # 시간표 생성
    schedules = generate_timetables(courses)

    print("생성된 시간표 개수:", len(schedules))

    # 생성된 시간표 출력 (간단 버전)
    for idx, s in enumerate(schedules):
        print(f"\n[{idx+1}]번째 시간표:")
        for c in s:
            print(f" - {c['name']} ({c['day']} {c['start']}~{c['end']})")


if __name__ == "__main__":
    main()
