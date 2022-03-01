from data.crud import get_all_passage_titles, get_all_poem_titles, get_all_author_names, \
    get_passages_by_author, get_passage_detail


def match(text: str) -> list:
    passages = []
    count = 0
    all_authors = get_all_author_names()
    for name in all_authors:
        if name in text or text in name:
            passages += get_passages_by_author(name)
            count += 1
            if count >= 6:
                return passages
    all_titles = get_all_poem_titles() + get_all_passage_titles()
    for title in all_titles:
        if text in title:
            passages.append(get_passage_detail(title).to_dict())
            count += 1
            if count >= 6:
                return passages
    return passages
