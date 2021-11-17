{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4060b492",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-11-17T05:18:16.632614Z",
     "start_time": "2021-11-17T05:18:16.617543Z"
    }
   },
   "outputs": [],
   "source": [
    "import re\n",
    "def cleansing(text):\n",
    "    gbg_lst = [\"_x000d_\",\"_x0_\",\"_x\"]\n",
    "    pattern1=re.compile('(\\[a-zA-Z0-9\\_.+-\\]+@\\[a-zA-Z0-9-\\]+.\\[a-zA-Z0-9-.\\]+)')  # e-mail 주소 제거 \n",
    "    pattern2=re.compile('(http|ftp|https)://(?:[-\\w.]|(?:\\da-fA-F]{2}))+' )   # url 제거\n",
    "    pattern3=re.compile('([ㄱ-ㅎㅏ-ㅣ])+') # 한글 자음, 모음 제거\n",
    "    pattern4=re.compile('<[^>]*>') # html tag 제거\n",
    "    pattern5=re.compile('[\\r|\\n]') # \\r, \\n 제거\n",
    "    pattern6=re.compile('[^\\w\\s%]')  # 특수기호 제거, %는 의미상 중요하므로 제외\n",
    "    pattern7=re.compile(r'\\s+') # 이중 space 제거\n",
    "    text=text.replace('(주)','').replace('(사)','')\n",
    "    text = re.sub(pattern=pattern1,repl=' ',string=text)\n",
    "    text = re.sub(pattern=pattern2,repl=' ',string=text)\n",
    "    text = re.sub(pattern=pattern3,repl=' ',string=text)\n",
    "    text = re.sub(pattern=pattern4,repl=' ',string=text)\n",
    "    text = re.sub(pattern=pattern5,repl=' ',string=text)\n",
    "    text = re.sub(pattern=pattern6,repl=' ',string=text)\n",
    "    text = re.sub(pattern=pattern7,repl=' ',string=text)\n",
    "    \n",
    "    # 가비지 데이터 제거\n",
    "    for g in gbg_lst:\n",
    "        text = text.replace(g,\"\")\n",
    "        \n",
    "    # 다중공백 제거\n",
    "    parseText = ' '.join(text.split()) \n",
    "    return(parseText)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
