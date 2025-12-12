# scheduler.py
# 시간표 생성 알고리즘

def is_conflict(a, b):
    """
    두 과목이 시간이 겹치는지 확인하는 함수
    """
    return a['day'] == b['day'] and not (a['end'] <= b['start'] or b['end'] <= a['start'])


def generate_timetables(courses):
    """
    가능한 모든 조합의 시간표를 생성하는 함수
    """
    result = []
    n = len(courses)

    def backtrack(idx, cur):
        if idx == n:
            result.append(cur[:])
            return

        # 현재 과목을 포함하는 경우
        conflict = False
        for c in cur:
            if is_conflict(c, courses[idx]):
                conflict = True
                break

        if not conflict:
            cur.append(courses[idx])
            backtrack(idx + 1, cur)
            cur.pop()

        # 현재 과목을 포함하지 않는 경우
        backtrack(idx + 1, cur)

    backtrack(0, [])
    return result
