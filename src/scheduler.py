from ortools.sat.python import cp_model

def generate_schedule(subjects, timeslots):
    model = cp_model.CpModel()

    # 변수 정의
    x = {}
    for s in subjects:
        for t in timeslots:
            x[(s, t)] = model.NewBoolVar(f"{s}_{t}")

    # 각 과목은 정확히 한 시간대에 배치
    for s in subjects:
        model.Add(sum(x[(s, t)] for t in timeslots) == 1)

    # 한 시간대에 두 과목이 동시에 배치되지 않도록
    for t in timeslots:
        model.Add(sum(x[(s, t)] for s in subjects) <= 1)

    solver = cp_model.CpSolver()
    solver.Solve(model)

    result = {}
    for s in subjects:
        for t in timeslots:
            if solver.Value(x[(s, t)]) == 1:
                result[s] = t
    
    return result
