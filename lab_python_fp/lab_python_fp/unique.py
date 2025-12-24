class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self._unique_items = []
        
        for item in items:
            if isinstance(item, str):
                if self.ignore_case:
                    if item not in self._unique_items:
                        self._unique_items.append(item)
                else:
                    item_lower = item.lower()
                    if not any(
                        isinstance(x, str) and x.lower() == item_lower
                        for x in self._unique_items
                    ):
                        self._unique_items.append(item)
            else:
                if item not in self._unique_items:
                    self._unique_items.append(item)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self._unique_items):
            raise StopIteration
        result = self._unique_items[self._index]
        self._index += 1
        return result

    def __str__(self):
        return str(self._unique_items)

    def __repr__(self):
        return f"Unique({self._unique_items})"

