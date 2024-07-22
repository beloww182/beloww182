# Testing the delete_record function
print("-" * 25)
delete_info = {
    'database': database,
    'table': 'contacts',
    'primary_key_field': 'contactid',
    'primary_key_value': '2'
}
delete_record(delete_info)

where_clause = ""
get_records(database, where_clause)

# Testing the update_record function
print("-" * 25)
update_info = {
    'database': database,
    'table': 'contacts',
    'primary_key_field': 'contactid',
    'primary_key_value': '3',
    'update_field': 'last',
    'new_value': 'Nelson'
}
update_record(update_info)

get_records(database, where_clause)
(1, 'Washington', 'George', '3200 Mount Vernon Memorial Highway', 'Mt. Vernon', 'VA', '22121')
(2, 'Lincoln', 'Abraham', '123 Main ST', 'Springfield', 'MO', '65803')
(3, 'Monroe', 'James', '2050 James Monroe Pkwy', 'Charlottesville', 'VA', '22902')
(2, 'Lincoln', 'Abraham', '123 Main ST', 'Springfield', 'MO', '65803')
(1, 'Washington', 'George', '3200 Mount Vernon Memorial Highway', 'Mt. Vernon', 'VA', '22121')
(3, 'Monroe', 'James', '2050 James Monroe Pkwy', 'Charlottesville', 'VA', '22902')
(1, 'Washington', 'George', '3200 Mount Vernon Memorial Highway', 'Mt. Vernon', 'VA', '22121')
(3, 'Nelson', 'Russell M.', '2050 James Monroe Pkwy', 'Charlottesville', 'VA', '22902')

