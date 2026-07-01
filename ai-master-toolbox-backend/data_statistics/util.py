from datetime import timedelta

def get_date_range(start_time, end_time):
    start_date = start_time.date()
    end_date = end_time.date()

    date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
    return date_range


def get_per_day_list_by_query_set(start_time, end_time, query_set):

    date_range = get_date_range(start_time, end_time)

    # 创建一个字典来存储结果
    result_dict = {}

    # 将实际数据与日期范围内的所有日期合并，确保不存在的日期 count 设置为 0
    for entry in query_set:
        date = entry['date']
        count = entry['count']
        result_dict[date] = count

    for date in date_range:
        if date not in result_dict:
            result_dict[date] = 0

    result = [{'date': k, 'count': result_dict[k]} for k in result_dict]
    result.sort(key=lambda e: e['date'])

    return result