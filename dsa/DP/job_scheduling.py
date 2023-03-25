def job_scheduling(starts, ends, profits):
    memo = {}
    jobs = sort_jobs(starts, ends, profits)
    return scheduling(jobs, 0, memo)


def sort_jobs(starts, ends, profits):
    return sorted(zip(starts, ends, profits), key=lambda tup: tup[0])


def get_next_job(jobs, start_time, pos):
    while pos > 0 and pos < len(jobs) and jobs[pos][0] < start_time:
        pos += 1
    return pos


def scheduling(jobs, pos, memo):
    if pos >= len(jobs):
        return 0
    if pos in memo:
        return memo[pos]

    next_job_index = get_next_job(jobs, jobs[pos][1], pos + 1)

    memo[pos] = max(
        jobs[pos][2] + scheduling(jobs, next_job_index, memo),
        scheduling(jobs, pos + 1, memo),
    )

    return memo[pos]
