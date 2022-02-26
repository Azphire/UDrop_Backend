from data.crud import get_all_passage_titles, get_all_poem_titles, get_all_author_names, \
    get_passages_by_author, get_passage_detail


def match(text: str) -> list:
    passages = []
    all_authors = get_all_author_names()
    for name in all_authors:
        if name in text:
            passages += get_passages_by_author(name)
    all_titles = get_all_poem_titles() + get_all_passage_titles()
    for title in all_titles:
        if text in title:
            passages.append(get_passage_detail(title).to_dict())
    return passages
