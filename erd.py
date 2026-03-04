import graphviz

# ERD 생성을 위한 Graphviz 객체 생성
dot = graphviz.Digraph('gym_project_erd', comment='Gym Project ERD')
dot.attr(rankdir='LR', size='12,12', splines='ortho')

# 노드 스타일 설정 (ERD 느낌)
dot.attr('node', shape='plain')

# 1. User Table
dot.node('user', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>user</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD>email</TD><TD>VARCHAR</TD></TR>
  <TR><TD>password</TD><TD>VARCHAR</TD></TR>
  <TR><TD>user_name</TD><TD>VARCHAR</TD></TR>
  <TR><TD>role</TD><TD>ENUM</TD></TR>
  <TR><TD>social_type</TD><TD>ENUM</TD></TR>
</TABLE>>''')

# 2. Gym Table
dot.node('gym', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>gym</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="user_id">user_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>name</TD><TD>VARCHAR</TD></TR>
  <TR><TD>address</TD><TD>VARCHAR</TD></TR>
  <TR><TD>registry_num</TD><TD>BIGINT</TD></TR>
</TABLE>>''')

# 3. Gym Product
dot.node('gym_product', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>gym_product</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="gym_id">gym_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>product_name</TD><TD>VARCHAR</TD></TR>
  <TR><TD>price</TD><TD>INT</TD></TR>
</TABLE>>''')

# 4. Gym Hour
dot.node('gym_hour', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>gym_hour</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="gym_id">gym_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>day_of_week</TD><TD>ENUM</TD></TR>
  <TR><TD>open/close</TD><TD>TIME</TD></TR>
</TABLE>>''')

# 5. Gym Hour Exception
dot.node('gym_hour_exception', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>gym_hour_exception</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="gym_id">gym_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>specific_date</TD><TD>DATE</TD></TR>
</TABLE>>''')

# 6. Gym Notice
dot.node('gym_notice', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>gym_notice</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="gym_id">gym_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>title</TD><TD>VARCHAR</TD></TR>
</TABLE>>''')

# 7. Amenity & Gym Amenity
dot.node('amenity', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>amenity</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD>name</TD><TD>VARCHAR</TD></TR>
</TABLE>>''')

dot.node('gym_amenity', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>gym_amenity</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="gym_id">gym_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="amenity_id">amenity_id (FK)</TD><TD>BIGINT</TD></TR>
</TABLE>>''')

# 8. Workout
dot.node('workout', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>workout</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="user_id">user_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>title</TD><TD>VARCHAR</TD></TR>
</TABLE>>''')

# 9. Post
dot.node('post', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>post</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="user_id">user_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="workout_id">workout_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>title</TD><TD>VARCHAR</TD></TR>
</TABLE>>''')

# 10. Post Comment & Like
dot.node('post_comment', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>post_comment</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="post_id">post_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="user_id">user_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="parent_id">parent_id (FK)</TD><TD>BIGINT</TD></TR>
</TABLE>>''')

dot.node('post_like', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>post_like</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="post_id">post_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="user_id">user_id (FK)</TD><TD>BIGINT</TD></TR>
</TABLE>>''')

# 11. Review
dot.node('review', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>review</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="user_id">user_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="gym_id">gym_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>rating</TD><TD>INT</TD></TR>
</TABLE>>''')

# 12. Chat
dot.node('chat_room', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>chat_room</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD>room_name</TD><TD>VARCHAR</TD></TR>
</TABLE>>''')

dot.node('chat_message', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>chat_message</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="room_id">chat_room_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="sender_id">sender_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>message</TD><TD>TEXT</TD></TR>
</TABLE>>''')

# 13. Others (Notification, Report, Image) - showing User connection primarily
dot.node('notification', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>notification</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="user_id">user_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>ref_type</TD><TD>VARCHAR</TD></TR>
</TABLE>>''')

dot.node('report', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>report</B></TD></TR>
  <TR><TD PORT="id"><B>id (PK)</B></TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="reporter_id">reporter_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD>ref_type</TD><TD>ENUM</TD></TR>
</TABLE>>''')

# Redis Table (Fav)
dot.node('gym_fav', '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightgrey"><B>gym_fav (Redis)</B></TD></TR>
  <TR><TD PORT="user_id">user_id (FK)</TD><TD>BIGINT</TD></TR>
  <TR><TD PORT="gym_id">gym_id (FK)</TD><TD>BIGINT</TD></TR>
</TABLE>>''')


# Relationships (Edges)
dot.edge('user:id', 'gym:user_id')
dot.edge('gym:id', 'gym_product:gym_id')
dot.edge('gym:id', 'gym_hour:gym_id')
dot.edge('gym:id', 'gym_hour_exception:gym_id')
dot.edge('gym:id', 'gym_notice:gym_id')
dot.edge('gym:id', 'gym_amenity:gym_id')
dot.edge('amenity:id', 'gym_amenity:amenity_id')

dot.edge('user:id', 'workout:user_id')
dot.edge('user:id', 'post:user_id')
dot.edge('workout:id', 'post:workout_id')

dot.edge('post:id', 'post_comment:post_id')
dot.edge('user:id', 'post_comment:user_id')
dot.edge('post_comment:id', 'post_comment:parent_id') # Self referencing

dot.edge('post:id', 'post_like:post_id')
dot.edge('user:id', 'post_like:user_id')

dot.edge('user:id', 'review:user_id')
dot.edge('gym:id', 'review:gym_id')

dot.edge('chat_room:id', 'chat_message:room_id')
dot.edge('user:id', 'chat_message:sender_id')

dot.edge('user:id', 'notification:user_id')
dot.edge('user:id', 'report:reporter_id')

dot.edge('user:id', 'gym_fav:user_id')
dot.edge('gym:id', 'gym_fav:gym_id')

print(dot.source)