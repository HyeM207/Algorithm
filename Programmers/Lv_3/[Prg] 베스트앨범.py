# 231221 성공
def solution(genres, plays):
    """
    장르 별로 가장 많이 재생된 노래 2개씩
    1. 많이 재생된 장르 먼저
        2. 노래많이 재생된 순, 고유 번호 낮은 순서대로
        
    장르별 노래 합산 필요
    => 키: 장르 value : [ [고유번호, 재생횟수] , ... ]
    
    1. 장르 정렬
    2. 재생 횟수별, 고유번호 별 곡 정렬 
    """
    from collections import Counter 
    answer = []
    genre_plays = {} # 장르 별 곡 고유번호와 재생 횟수 저장
    genre_cnt = {} # 장르 별 플레이 횟수 총 합산
    
    # 1. 딕셔너리화
    for idx, (genre, cnt) in enumerate(zip(genres, plays)):
        genre_plays[genre] = genre_plays.get(genre, []) + [[idx, cnt]]
        genre_cnt[genre] = genre_cnt.get(genre, 0) + cnt

    # 2. 장르 정렬과 노래 정렬
    most_genres = [key for key, _ in Counter(genre_cnt).most_common()]
    for genre in most_genres:
        for id, cnt in sorted(genre_plays[genre], key=lambda x: (x[1], -x[0]), reverse=True)[:2]:
            answer.append(id) 
    
    return answer
