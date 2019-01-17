# Click Through Rate map reduce
def mapper(key=None, value=log):
    if log.is_shown:
        yield log.ad_id, log.is_click
        # use key = -1 to summarize overall CTR
        yield -1, log.is_click

def reducer(key, value_iterator):
    clicks = 0
    counts = 0
    while value_iterator.has_next():
        click = value_iterator.next()
        clicks += click
        counts +=  1
    yield key, clicks / float(counts)
