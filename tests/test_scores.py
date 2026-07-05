rom src.scores import summarize_scores

def test_normal_scores():
    result = summarize_scores([80, 35, 60])

    assert result["total_count"] == 3
    assert result["passed_count"] == 2
    assert result["failed_count"] == 1
    assert result["average_score"] == 175 / 3
