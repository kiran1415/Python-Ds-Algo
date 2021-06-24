class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        source  =  image[sr][sc]
        if source == newColor:
            return image
        self.dfs(image, sr, sc, newColor, rows, cols, source)
        return image
        
    def dfs(self,image,sr,sc,newColor,rows,cols,source):
        if sr < 0 or sr >= rows or sc<0 or sc >= cols:
            return
        elif image[sr][sc] != source:
            return
        image[sr][sc] = newColor
        self.dfs(image,sr-1,sc,newColor,rows,cols,source)
        self.dfs(image,sr+1,sc,newColor,rows,cols,source)
        self.dfs(image,sr,sc-1,newColor,rows,cols,source)
        self.dfs(image,sr,sc+1,newColor,rows,cols,source)
        
        