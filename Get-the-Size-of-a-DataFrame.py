1import pandas as pd
2
3def getDataframeSize(players: pd.DataFrame) -> List[int]:
4    return [players.shape[0], players.shape[1]]
5    