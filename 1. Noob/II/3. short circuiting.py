# Short circuiting
is_friend = True
is_user = True

if is_friend or is_user:  # this is a disjunction, meanwhile the 'and' is a conjunction
    print('besto friendo')
