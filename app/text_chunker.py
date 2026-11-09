def _split_by_separators(text: str, chunk_size: int, separators: list[str]) -> list[str]:
    if len(text) <= chunk_size:
        return [text.strip()]

    if not separators:
        return [
            text[index:index + chunk_size].strip()
            for index in range(0, len(text), chunk_size)
        ]

    separator = separators[0]
    parts = text.split(separator)

    if len(parts) == 1:
        return _split_by_separators(text, chunk_size, separators[1:])

    pieces = []

    for part in parts:
        part = part.strip()

        if part:
            pieces.extend(
                _split_by_separators(part, chunk_size, separators[1:])
            )

    return pieces


def split_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[str]:
    """Split text using natural boundaries and controlled overlap."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "overlap must be non-negative and smaller than chunk_size"
        )

    separators = ["\n\n", "\n", ". ", " ", ""]
    pieces = _split_by_separators(text.strip(), chunk_size, separators)

    chunks = []
    current = ""

    for piece in pieces:
        candidate = f"{current} {piece}".strip()

        if current and len(candidate) > chunk_size:
            chunks.append(current)

            overlap_text = current[-overlap:].strip()
            current = f"{overlap_text} {piece}".strip()
        else:
            current = candidate

    if current:
        chunks.append(current)

    return chunks