# (ex. 4.8. - Netflix)

def title_best_score(filename: str) -> tuple:
    """return the title with the highest score

    Args:
        filename (str): name or absolute path of the file

    Returns:
        tuple: (best title, best score)
    """
    with open(filename) as fp:
        
        best_score = 0
        best_title = ""

        for line in fp:
            title, genre, year, score, date = line.strip().split(",")

            try:
                score = float(score)
            except ValueError:
                continue

            if score > best_score:
                best_score = score
                best_title = title

        return best_title, best_score

def avg_drama(filename: str) -> int:
    """return the average score of genre Drama

    Args:
        filename (str): name or absolute path of file

    Returns:
        int: average score of genre Drama
    """
    with open(filename) as fp:
        scores = 0
        drama_count = 0

        for line in fp:
            title, genre, year, score, date = line.strip().split(",")

            if genre == "Drama":
                drama_count += 1
                try:
                    score = float(score)
                    scores += score
                except ValueError:
                    continue

    return f"{(scores / drama_count):.2f}"

def append_record(filename: str):
    with open(filename, "a") as fp:
        fp.write("Happy coder, Drama, 2023, 9.9, 2023")