class CityValidator:
    def __init__(self, grid_data):
        """
        コンストラクタ
        :param grid_data: 5x5の高さデータ（リストのリスト）
        """
        self.grid = grid_data
        self.rows = len(grid_data)
        self.cols = len(grid_data[0])

    def check_sunlight(self):
        """
        要件A：日照権チェック
        南側の建物(r+1)が、自分(r)以上の高さの場合、日当たりが悪いと判定。
        :return: 該当する区画の座標リスト [(r, c), ...]
        """
        violations = [] # 1. ここで箱を用意する

        # 2. ループ処理（ここをそのまま書く）
        for r in range(self.rows - 1):
            for c in range(self.cols):
                north_height = self.grid[r][c]
                south_height = self.grid[r + 1][c]
                
                # 北にも南にも建物がある場合
                if north_height > 0 and south_height > 0:
                    if north_height <= south_height:
                        # 3. 箱に追加する
                        violations.append((r, c))
        
        # 4. 最後に箱を返す
        return violations

    def find_crowded_zones(self, threshold):
        """
        要件B：過密エリア特定
        自身＋東西南北の高さ合計がthresholdを超える区画を探す。
        :param threshold: 過密判定の基準値（整数）
        :return: 辞書 {(r, c): total_height, ...}
        """
        crowded_spots = {}
        # ここに処理を記述してください

        for r in range(self.rows):
            for c in range(self.cols):
                # 1. まず自分を足す
                total = self.grid[r][c]

                # 2. 北（上）
                if r > 0:
                    total += self.grid[r - 1][c]
                
                # 3. 南（下）
                if r < self.rows - 1:
                    total += self.grid[r + 1][c]
                
                # 4. 西（左）
                if c > 0:
                    total += self.grid[r][c - 1]
                
                # 5. 東（右）
                if c < self.cols - 1: # self.colsと比較
                    total += self.grid[r][c + 1]
                  
                if total > threshold:
                  crowded_spots[(r,c)] = total
                  
        return crowded_spots

# --- 実行・検証用コード（変更不要） ---
if __name__ == "__main__":
    # テストデータ
    test_area = [
        [0, 10, 5, 0, 8],   # 行0
        [0, 12, 6, 0, 8],   # 行1
        [5, 15, 0, 0, 10],  # 行2
        [5, 5,  0, 0, 5],   # 行3
        [0, 0,  0, 0, 0]    # 行4
    ]

    validator = CityValidator(test_area)

    # 1. 日照権チェックの実行
    print("--- 日照権チェック ---")
    sunlight_issues = validator.check_sunlight()
    print(f"日照権侵害リスト: {sunlight_issues}")
    # 期待される出力例: [(0, 1), (1, 2), (2, 4)] など（ロジックに基づいて計算してください）

    # 2. 過密エリアチェックの実行
    print("\n--- 過密エリアチェック (閾値: 30) ---")
    crowded = validator.find_crowded_zones(30)
    print(f"過密エリア: {crowded}")
    # 期待される出力例: {(1, 1): 37, (2, 1): 32} など