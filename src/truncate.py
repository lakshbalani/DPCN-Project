import pandas as pd

def split_data_ranges(start, end, num_parts):
    total_rows = end - start + 1
    rows_per_part = total_rows // num_parts
    remaining_rows = total_rows % num_parts

    ranges = []
    current_row = start
    for i in range(num_parts):
        part_size = rows_per_part + (1 if i < remaining_rows else 0)
        part_end = current_row + part_size - 1
        ranges.append((current_row, part_end))
        current_row = part_end + 1

    return ranges

df = pd.read_csv('233_filtered.csv')

ranges = []

ranges.extend(split_data_ranges(23588, 28587, 2))

ranges.extend(split_data_ranges(28588, 44167, 10))

ranges.extend(split_data_ranges(44168, 49167, 2))

for i, (start, end) in enumerate(ranges, start=1):
    print(f"Part {i}: Rows {start} to {end}") # type: ignore

# make entire csv for each section

for i, (start, end) in enumerate(ranges, start=1):
    df_part = df.iloc[start:end+1]
    df_part.to_csv(f'233_part_{i}.csv', index=False)
    print(f"Part {i} saved to 233_part_{i}.csv") # type: ignore

# df = pd.read_csv('234.csv')

# ranges = []

# ranges.extend(split_data_ranges(23029, 28028, 2))

# ranges.extend(split_data_ranges(28029, 53071, 10))

# ranges.extend(split_data_ranges(53072, 58071, 2))

# for i, (start, end) in enumerate(ranges, start=1):
#     print(f"Part {i}: Rows {start} to {end}") # type: ignore

# # make entire csv for each section

# for i, (start, end) in enumerate(ranges, start=1):
#     df_part = df.iloc[start:end+1]
#     df_part.to_csv(f'234_part_{i}.csv', index=False)
#     print(f"Part {i} saved to 234_part_{i}.csv") # type: ignore