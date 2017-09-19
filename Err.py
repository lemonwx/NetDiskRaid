errors = {
    -9 : 'Fail, no such dictionarys', # ls 
    -7 : "Fail, params not incorrect",
    31047 : 'Fail, user must relogin', # upload's upload file by payload and get md5, maybe cookie not correct
    2 : 'Fail, data not incorrect', # upload's create file by md5, maybe md5 or file_sz not matching 
    -6 : "Fail, maybe create file's cookie not incorrect", # upload's create file by md5, maybe cookie not incorrect
}