def summarize_scores(scores):
    total_count = len(scores)
    passed_count = sum(1 for score in scores if score >= 40)
    failed_count = total_count - passed_count
    average_score = sum(scores) / total_count

    return {
        "total_count": total_count,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "average_score": average_score,
    }
