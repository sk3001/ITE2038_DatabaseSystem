import sys
import pymysql as pms

connection = pms.connect(
    host = '127.0.0.1',
    port = 3307,
    user = 'root',
    password = '111111',
    db = 'music_app',
    charset = 'utf8'
)

cursor = connection.cursor()

def administratorMenu():
    while True:
        print('\n0: Return to Previous Menu')
        print('1: Enroll Music')
        print('2: Delete Music')
        print('3: Manage Users')
        print('4: Search Music')
        print('5. Show all Music')

        x = input("Input: ")

        if x=='0':
            return
        elif x=='1':
            enrollMusic()
        elif x=='2':
            deleteMusic()
        elif x=='3':
            managingUsers()
        elif x=='4':
            searchMusic()
        elif x=='5':
            musicDetails()
        else:
            exit(0)

def enrollMusic():
    try:
        sql = "INSERT INTO music(NAME, INFO, ID, LYRICS, COMPOSE, ALBUMID, ENROLL_ID, DELETE_ID, ARTISTID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        a = input('Name: ')
        b = input('Info: ')
        c = input('ID: ')
        d = input('Lyrics: ')
        e = input('Compose: ')
        f = input('Album ID: ')
        g = input('Enroll ID: ')
        h = input('Delete ID: ')
        i = input('Artist ID: ')

        cursor.execute(sql, (a, b, c, d, e, f, g, h, i))
        connection.commit()

        cursor.execute("SELECT NAME FROM music where id=%s", c)
        rows = cursor.fetchall()

        for row in rows:
            print(row[0], "enroll completed!")
    
    except Exception as ex:
        print('Error occurred while enrolling music', ex)

def deleteMusic():
    try:
        a = input("ID: ")

        sql = "SELECT NAME FROM music WHERE ID=%s"
        cursor.execute(sql, a)
        
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row[0], "delete completed!")

        else:
            print('Error occurred while deleting music')
            return

        sql = "DELETE FROM belong_to_playlist_music WHERE MID=%s"
        cursor.execute(sql, a)
        connection.commit()

        sql = "DELETE FROM has_music_genre WHERE MID=%s"
        cursor.execute(sql, a)
        connection.commit()

        sql = "DELETE FROM heard WHERE MID=%s"
        cursor.execute(sql, a)
        connection.commit()

        sql = "DELETE FROM preferred_music WHERE MID=%s"
        cursor.execute(sql, a)
        connection.commit()

        sql = "DELETE FROM music WHERE ID=%s"
        cursor.execute(sql, a)
        connection.commit()

    except Exception as ex:
        print('Error occurred while deleting music', ex)

def managingUsers():
    while True:
        print('\n0. Return to Previous Menu')
        print('1. Enroll User')
        print('2. Delete User')
        print('3. View Users')

        x = input('Input: ')

        if x=='0':
            return
        elif x=='1':
            enrollUser()
        elif x=='2':
            deleteUser()
        elif x=='3':
            viewUsers()
        else:
            exit(0)

def enrollUser():
    try:
        sql = "INSERT INTO user(NAME, ID, PASSWORD, NICKNAME, GENDER, MNG_ID, SIGN_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        a = input('Name: ')
        b = input('ID: ')
        c = input('Password: ')
        d = input('Nickname: ')
        e = input('Gender: ')
        f = input('Manage ID: ')
        g = input('Sign ID: ')

        cursor.execute(sql, (a, b, c, d, e, f, g))
        connection.commit()

        sql = "SELECT NAME FROM user where ID=%s"
        cursor.execute(sql, b)

        rows = cursor.fetchall()
        for row in rows:
            print(row[0], "enrolled completed!")
    
    except Exception as ex:
        print('Error occurred while enrolling user', ex)

def deleteUser():
    try:
        a = int(input("ID: "))

        sql = "SELECT NAME FROM user WHERE ID=%s"
        cursor.execute(sql, a)
        
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row[0], "delete completed!")
        
        else:
            print('Error occurred while deleting user')
            return

        sql = "DELETE FROM playlist WHERE UID=%s"
        cursor.execute(sql, a)
        connection.commit()

        sql = "DELETE FROM preferred_music WHERE UID=%s"
        cursor.execute(sql, a)
        connection.commit()

        sql = "DELETE FROM heard WHERE UID=%s"
        cursor.execute(sql, a)
        connection.commit()

        sql = "DELETE FROM preferred_artist WHERE UID=%s"
        cursor.execute(sql, a)
        connection.commit()

        sql = "DELETE FROM preferred_genre WHERE UID=%s"
        cursor.execute(sql, a)
        connection.commit()

        sql = "DELETE FROM user WHERE ID=%s"
        cursor.execute(sql, a)
        connection.commit()

    except Exception as ex:
        print('Error occurred while deleting user', ex)

def viewUsers():
    sql = "SELECT * FROM user"
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        print('Name:', row[0], 'ID:', row[1], 'Password:', row[2], 'Nickname:', row[3], 'Gender:', row[4], 'ManageID:', row[5], 'SignID:', row[6])

def userMenu():
    while True:
        print('\n0. Return to Previous Menu')
        print('1. Sign Up')
        print('2. Log In')

        x = input('Input: ')

        if x=='0':
            return
        elif x=='1':
            signUp()
        elif x=='2':
            logIn()   
        else:
            exit(0)

def signUp():
    try:
        sql = "INSERT INTO user(NAME, ID, PASSWORD, NICKNAME, GENDER, MNG_ID, SIGN_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        a = input('Name: ')
        b = input('ID: ')
        c = input('Password: ')
        d = input('Nickname: ')
        e = input('Gender: ')
        f = input('Manage ID: ')
        g = input('Sign ID: ')

        cursor.execute(sql, (a, b, c, d, e, f, g))
        connection.commit()

        sql = "SELECT NAME FROM user where ID=%s"
        cursor.execute(sql, b)

        rows = cursor.fetchall()
        for row in rows:
            print(row[0], "signed up completed!")
    
    except Exception as ex:
        print('Error occurred while signing up', ex)

def logIn():
    sql = "SELECT NAME, ID FROM user WHERE ID=%s AND PASSWORD=%s"
    a = input('ID: ')
    b = input('Password: ')

    cursor.execute(sql, (a, b))
    rows = cursor.fetchall()
    for row in rows:
        print("Name:", row[0], "ID:", row[1], "logged in!")
    
    if rows:
        realUserMenu(a)

    print('ID or Password Error!')

def realUserMenu(a):
    while True:
        print('\n0. Return to Previous Menu')
        print('1. Playlist Menu')
        print('2. Preference Menu')
        print('3. View Music Information')

        x = input('Input: ')

        if x=='0':
            return
        elif x=='1':
            playlistMenu(a)
        elif x=='2':
            preferenceMenu(a)
        elif x=='3':
            viewMusic(a) 
        else:
            exit(0)

def playlistMenu(a):
    while True:
        print('\n0. Return to Previous Menu')
        print('1. Create Playlist')
        print('2. Delete Playlist')
        print('3. Add Music to Playlist')
        print('4. Delete Music from Playlist')
        print('5. View my Playlists')
        print('6. View all Playlists')
        print('7. View Details of Playlists')

        x = input('Input: ')

        if x=='0':
            return
        elif x=='1':
            createPlaylist(a)
        elif x=='2':
            deletePlaylist(a)
        elif x=='3':
            addToPlaylist(a)
        elif x=='4':
            deleteFromPlaylist(a)
        elif x=='5':
            viewMyPlaylists(a)
        elif x=='6':
            viewPlaylists()
        elif x=='7':
            viewDetailPlaylists()
        else:
            exit(0)

def createPlaylist(a):
    try:
        sql = "INSERT INTO playlist(UID, NAME, ID) VALUES (%s,%s,%s)"

        b = input('Name: ')
        c = input('Playlist ID:')

        cursor.execute(sql, (a, b, c))
        connection.commit()

        cursor.execute("SELECT NAME FROM playlist where UID=%s AND ID=%s", (a, c))
        rows = cursor.fetchall()

        for row in rows:
            print(row[0], "create completed!")
    
    except Exception as ex:
        print('Error occurred while creating playlist', ex)

def deletePlaylist(a):
    try:
        b = input("Playlist ID: ")

        sql = "SELECT NAME FROM playlist WHERE ID=%s AND UID=%s"
        cursor.execute(sql, (b, a))
        
        rows = cursor.fetchall()

        for row in rows:
            print(row[0], "delete completed!")

        sql = "DELETE FROM belong_to_playlist_music WHERE PID=%s"
        cursor.execute(sql, b)
        connection.commit()

        sql = "DELETE FROM playlist WHERE ID=%s"
        cursor.execute(sql, b)
        connection.commit()

    except Exception as ex:
        print('Error occurred while deleting playlist', ex)

def addToPlaylist(a):
    try:
        sql = "INSERT INTO belong_to_playlist_music(MID, PID) VALUES (%s,%s)"

        b = input('Music ID: ')
        c = input('Playlist ID: ') 

        cursor.execute(sql, (b, c))
        connection.commit()

        cursor.execute("SELECT music.NAME, playlist.NAME FROM music, playlist where playlist.UID=%s AND music.ID=%s AND playlist.ID=%s", (a,b,c))
        rows = cursor.fetchall()

        for row in rows:
            print("Adding", row[0], "to", row[1], "completed!")
    
    except Exception as ex:
        print('Error occurred while adding music to playlist', ex)

def deleteFromPlaylist(a):
    try:
        b = input('Music ID: ')
        c = input('Playlist ID:')

        cursor.execute("SELECT music.NAME, playlist.NAME FROM music, playlist, belong_to_playlist_music where music.ID=belong_to_playlist_music.MID AND playlist.ID=belong_to_playlist_music.PID AND belong_to_playlist_music.MID=%s AND belong_to_playlist_music.PID=%s", (b, c))
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print("Deleting", row[0], "from", row[1], "completed!")

        else:
            print('Error occurred while deleting music from playlist')
            return

        sql = "DELETE FROM belong_to_playlist_music WHERE MID=%s AND PID=%s"

        cursor.execute(sql, (b, c))
        connection.commit()

    except Exception as ex:
        print('Error occurred while deleting music from playlist', ex)

def viewMyPlaylists(a):
    sql = "SELECT playlist.NAME, playlist.ID FROM playlist WHERE playlist.UID=%s"
    cursor.execute(sql, a)

    rows = cursor.fetchall()
    for row in rows:
        print(row[0], "ID:", row[1])

def viewPlaylists():
    sql = "SELECT user.NAME, playlist.NAME, playlist.ID FROM user, playlist where user.ID=playlist.UID"
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        print(row[0], ":", row[1], "ID:", row[2])

def viewDetailPlaylists():
    a = input("Playlist ID: ")
    sql = "SELECT music.NAME FROM music, playlist, belong_to_playlist_music where music.ID=belong_to_playlist_music.MID AND playlist.ID=belong_to_playlist_music.PID AND belong_to_playlist_music.PID=%s"
    cursor.execute(sql, a)

    rows = cursor.fetchall()
    for row in rows:
        print(row[0])

def preferenceMenu(a):
    while True:
        print('\n0. Return to Previous Menu')
        print('1. Preferred Artist')
        print('2. Preferred Genre')
        print('3. Preferred Music')

        x = input('Input: ')

        if x=='0':
            return
        elif x=='1':
            preferredArtist(a)
        elif x=='2':
            preferredGenre(a)
        elif x=='3':
            preferredMusic(a) 
        else:
            exit(0)

def preferredArtist(a):
    while True:
        print('\n0. Return to Previous Menu')
        print('1. Add')
        print('2. Delete')
        print('3. View')

        x = input('Input: ')

        if x=='0':
            return
        elif x=='1':
            try:
                sql = "INSERT INTO preferred_artist(UID, ARTISTID) VALUES (%s, %s)"

                b = input('Artist ID:')

                cursor.execute(sql, (a, b))
                connection.commit()

                cursor.execute("SELECT NAME FROM artist where ID=%s", b)
                rows = cursor.fetchall()

                for row in rows:
                    print(row[0], "add completed!")
            
            except Exception as ex:
                print('Error occurred while adding artist', ex)
        elif x=='2':
            try:
                b = input("Artist ID: ")

                sql = "SELECT NAME FROM artist WHERE ID=%s"
                cursor.execute(sql, b)
                
                rows = cursor.fetchall()

                for row in rows:
                    print(row[0], "delete completed!")

                sql = "DELETE FROM preferred_artist WHERE ARTISTID=%s"
                cursor.execute(sql, b)
                connection.commit()

            except Exception as ex:
                print('Error occurred while deleting artist', ex)
        elif x=='3':
            sql = "SELECT artist.NAME FROM artist, preferred_artist WHERE preferred_artist.UID=%s AND artist.ID=preferred_artist.ARTISTID"
            cursor.execute(sql, a)
            
            rows = cursor.fetchall()

            for row in rows:
                print(row[0]) 
        else:
            exit(0)

def preferredGenre(a):
    while True:
        print('\n0. Return to Previous Menu')
        print('1. Add')
        print('2. Delete')
        print('3. View')

        x = input('Input: ')

        if x=='0':
            return
        elif x=='1':
            try:
                sql = "INSERT INTO preferred_genre(UID, GNAME) VALUES (%s, %s)"

                b = input('Genre Name:')

                cursor.execute(sql, (a, b))
                connection.commit()

                cursor.execute("SELECT NAME FROM genre where NAME=%s", b)
                rows = cursor.fetchall()

                for row in rows:
                    print(row[0], "add completed!")
            
            except Exception as ex:
                print('Error occurred while adding genre', ex)
        elif x=='2':
            try:
                b = input("Genre Name: ")

                sql = "SELECT NAME FROM genre WHERE NAME=%s"
                cursor.execute(sql, b)
                
                rows = cursor.fetchall()

                for row in rows:
                    print(row[0], "delete completed!")

                sql = "DELETE FROM preferred_genre WHERE GNAME=%s"
                cursor.execute(sql, b)
                connection.commit()

            except Exception as ex:
                print('Error occurred while deleting genre', ex)
        elif x=='3':
            sql = "SELECT NAME FROM genre, preferred_genre WHERE preferred_genre.UID=%s AND genre.NAME=preferred_genre.GNAME"
            cursor.execute(sql, a)
            
            rows = cursor.fetchall()

            for row in rows:
                print(row[0]) 
        else:
            exit(0)

def preferredMusic(a):
    while True:
        print('\n0. Return to Previous Menu')
        print('1. Add')
        print('2. Delete')
        print('3. View')

        x = input('Input: ')

        if x=='0':
            return
        elif x=='1':
            try:
                sql = "INSERT INTO preferred_music(MID, UID) VALUES (%s, %s)"

                b = input('Music ID:')

                cursor.execute(sql, (b, a))
                connection.commit()

                cursor.execute("SELECT NAME FROM music where ID=%s", b)
                rows = cursor.fetchall()

                for row in rows:
                    print(row[0], "add completed!")
            
            except Exception as ex:
                print('Error occurred while adding music', ex)
        elif x=='2':
            try:
                b = input("Music ID: ")

                sql = "SELECT NAME FROM music WHERE ID=%s"
                cursor.execute(sql, b)
                
                rows = cursor.fetchall()

                for row in rows:
                    print(row[0], "delete completed!")

                sql = "DELETE FROM preferred_music WHERE MID=%s"
                cursor.execute(sql, b)
                connection.commit()

            except Exception as ex:
                print('Error occurred while deleting music', ex)
        elif x=='3':
            sql = "SELECT NAME FROM music, preferred_music WHERE preferred_music.UID=%s AND music.ID=preferred_music.MID"
            cursor.execute(sql, a)
            
            rows = cursor.fetchall()

            for row in rows:
                print(row[0]) 
        else:
            exit(0)

def viewMusic(a):
    while True:
        print('\n0. Return to Previous Menu')
        print('1. Recent Heard')
        print('2. Mostly Heard')
        print('3. Listen to Music')
        print('4. Search Music')
        print('5. Show Music Details')

        x = input('Input: ')

        if x=='0':
            return
        elif x=='1':
            recentHeard(a)
        elif x=='2':
            mostlyHeard()
        elif x=='3':
            listenToMusic(a)
        elif x=='4':
            searchMusic() 
        elif x=='5':
            musicDetails() 
        else:
            exit(0)

def recentHeard(a):
    sql = "SELECT music.name, heard.date FROM music, heard where heard.UID=%s AND heard.MID=music.ID order by heard.date DESC"
    cursor.execute(sql, a)

    rows = cursor.fetchall()
    print(rows[0][0], "Date:", rows[0][1])

def mostlyHeard():
    sql = "SELECT heard.MID, COUNT(*) FROM heard GROUP BY heard.MID order by count(*) desc"
    cursor.execute(sql)

    rows = cursor.fetchall()
    a = rows[0][0]
    b = rows[0][1]

    sql = "SELECT music.NAME FROM music where music.ID=%s"
    cursor.execute(sql, a)

    rows = cursor.fetchall()
    print(rows[0][0], "Heard Times:", b)

def listenToMusic(a):
    try:
        sql = "INSERT INTO heard(UID, MID, Date) VALUES (%s,%s,%s)"

        b = input('Music ID: ')
        c = input('Date:')

        cursor.execute(sql, (a, b, c))
        connection.commit()

        cursor.execute("SELECT NAME FROM music where music.ID=%s", b)
        rows = cursor.fetchall()

        for row in rows:
            print(row[0], "listen completed!")
    
    except Exception as ex:
        print('Error occurred while listening to music', ex)

def searchMusic():
    a = input("Music Name:")
    sql = "SELECT music.NAME, INFO, music.ID, artist.NAME, LYRICS, COMPOSE, album.name FROM music, album, artist WHERE music.NAME=%s AND music.ALBUMID=album.ID AND music.ARTISTID=artist.ID"
    cursor.execute(sql, a)
    
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print("Name:", row[0], "Info:", row[1], "Music ID:", row[2],"Artist:", row[3], "Lyrics:", row[4], "Composer:", row[5], "Album:", row[6])
    else:
        print('No music found!')

def musicDetails():
    sql = "SELECT music.NAME, INFO, music.ID, artist.NAME, LYRICS, COMPOSE, album.name FROM music, album, artist WHERE music.ALBUMID=album.ID AND music.ARTISTID=artist.ID"
    cursor.execute(sql)
    
    rows = cursor.fetchall()

    for row in rows:
        print("Name:", row[0], "Info:", row[1], "Music ID:", row[2],"Artist:", row[3], "Lyrics:", row[4], "Composer:", row[5], "Album:", row[6])

def main():
    while True:
        print('\n0. Exit')
        print('1. Administrator Menu')
        print('2. User Menu')

        x = input('Input: ')

        if x=='0':
            exit(0)
        elif x=='1':
            administratorMenu()
        elif x=='2':
            userMenu()
        else:
            exit(0)

main()