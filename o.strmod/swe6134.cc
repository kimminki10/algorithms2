#include <stdio.h>
#include <string.h>

typedef enum { CMD_INIT, CMD_ADD, CMD_DELETE, CMD_CHANGE, CMD_SEARCH } COMMAND;

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
typedef enum { NAME, NUMBER, BIRTHDAY, EMAIL, MEMO } FIELD;

typedef struct {
    int count;
    char str[20];
} RESULT;

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
#include <map>
#include <string>
#include <vector>

using namespace std;

struct Record {
    string NAME;
    string NUMBER;
    string BIRTHDAY;
    string EMAIL;
    string MEMO;
    bool isDel = false;
};

multimap<string, Record*> mmNAME;
multimap<string, Record*> mmNUMBER;
multimap<string, Record*> mmBIRTHDAY;
multimap<string, Record*> mmEMAIL;
multimap<string, Record*> mmMEMO;

void InitDB() {
    mmNAME = {};
    mmNUMBER = {};
    mmBIRTHDAY = {};
    mmEMAIL = {};
    mmMEMO = {};
}

void Add(char* name, char* number, char* birthday, char* email, char* memo) {
    Record* re = new Record();
    re->NAME = string(name);
    re->NUMBER = string(number);
    re->BIRTHDAY = string(birthday);
    re->EMAIL = string(email);
    re->MEMO = string(memo);

    mmNAME.insert({re->NAME, re});
    mmNUMBER.insert({re->NUMBER, re});
    mmBIRTHDAY.insert({re->BIRTHDAY, re});
    mmEMAIL.insert({re->EMAIL, re});
    mmMEMO.insert({re->MEMO, re});
}

int Delete(FIELD field, char* str) {
    int result = 0;
    string s = string(str);
    multimap<string, Record*>::iterator l, r;
    if (field == NAME) {
        l = mmNAME.lower_bound(s);
        r = mmNAME.upper_bound(s);
    }
    if (field == NUMBER) {
        l = mmNUMBER.lower_bound(s);
        r = mmNUMBER.upper_bound(s);
    }
    if (field == BIRTHDAY) {
        l = mmBIRTHDAY.lower_bound(s);
        r = mmBIRTHDAY.upper_bound(s);
    }
    if (field == EMAIL) {
        l = mmEMAIL.lower_bound(s);
        r = mmEMAIL.upper_bound(s);
    }
    if (field == MEMO) {
        l = mmMEMO.lower_bound(s);
        r = mmMEMO.upper_bound(s);
    }
    Record* re;

    for (auto i = l; i != r; i++) {
        re = i->second;
        if (re->isDel == false) {
            re->isDel = true;
            result++;
        }
    }
    return result;
}

int Change(FIELD field, char* str, FIELD changefield, char* changestr) {
    int result = 0;
    string s = string(str);
    multimap<string, Record*>::iterator l, r;
    if (field == NAME) {
        l = mmNAME.lower_bound(s);
        r = mmNAME.upper_bound(s);
    }
    if (field == NUMBER) {
        l = mmNUMBER.lower_bound(s);
        r = mmNUMBER.upper_bound(s);
    }
    if (field == BIRTHDAY) {
        l = mmBIRTHDAY.lower_bound(s);
        r = mmBIRTHDAY.upper_bound(s);
    }
    if (field == EMAIL) {
        l = mmEMAIL.lower_bound(s);
        r = mmEMAIL.upper_bound(s);
    }
    if (field == MEMO) {
        l = mmMEMO.lower_bound(s);
        r = mmMEMO.upper_bound(s);
    }
    Record* re;
    vector<Record*> addv;
    for (auto i = l; i != r; i++) {
        re = i->second;
        if (re->isDel == false) {
            re->isDel = true;
            result++;
            if (changefield == NAME) {
                re->NAME = string(changestr);
            }
            if (changefield == NUMBER) {
                re->NUMBER = string(changestr);
            }
            if (changefield == BIRTHDAY) {
                re->BIRTHDAY = string(changestr);
            }
            if (changefield == EMAIL) {
                re->EMAIL = string(changestr);
            }
            if (changefield == MEMO) {
                re->MEMO = string(changestr);
            }
            addv.push_back(re);
        }
    }
    for (int i = 0; i < (int)addv.size(); i++) {
        re = addv[i];
        Add((char*)re->NAME.c_str(), (char*)re->NUMBER.c_str(),
            (char*)re->BIRTHDAY.c_str(), (char*)re->EMAIL.c_str(),
            (char*)re->MEMO.c_str());
    }
    return result;
}

RESULT Search(FIELD field, char* str, FIELD ret_field) {
    RESULT result;
    result.count = 0;
    string s = string(str);
    multimap<string, Record*>::iterator l, r;
    if (field == NAME) {
        l = mmNAME.lower_bound(s);
        r = mmNAME.upper_bound(s);
    }
    if (field == NUMBER) {
        l = mmNUMBER.lower_bound(s);
        r = mmNUMBER.upper_bound(s);
    }
    if (field == BIRTHDAY) {
        l = mmBIRTHDAY.lower_bound(s);
        r = mmBIRTHDAY.upper_bound(s);
    }
    if (field == EMAIL) {
        l = mmEMAIL.lower_bound(s);
        r = mmEMAIL.upper_bound(s);
    }
    if (field == MEMO) {
        l = mmMEMO.lower_bound(s);
        r = mmMEMO.upper_bound(s);
    }
    Record* re;

    for (auto i = l; i != r; i++) {
        re = i->second;
        if (re->isDel == false) {
            result.count++;
            if (ret_field == NAME) {
                strcpy(result.str, re->NAME.c_str());
            }
            if (ret_field == NUMBER) {
                strcpy(result.str, re->NUMBER.c_str());
            }
            if (ret_field == BIRTHDAY) {
                strcpy(result.str, re->BIRTHDAY.c_str());
            }
            if (ret_field == EMAIL) {
                strcpy(result.str, re->EMAIL.c_str());
            }
            if (ret_field == MEMO) {
                strcpy(result.str, re->MEMO.c_str());
            }
        }
    }
    return result;
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

static int dummy[100];
static int Score, ScoreIdx;
static char name[20], number[20], birthday[20], email[20], memo[20];

static char lastname[10][5] = {"kim",  "lee", "park", "choi", "jung",
                               "kang", "cho", "oh",   "jang", "lim"};
static int lastname_length[10] = {3, 3, 4, 4, 4, 4, 3, 2, 4, 3};

static int mSeed;
static int mrand(int num) {
    mSeed = mSeed * 1103515245 + 37209;
    if (mSeed < 0) mSeed *= -1;
    return ((mSeed >> 8) % num);
}

static void make_field(int seed) {
    int name_length, email_length, memo_length;
    int idx, num;

    mSeed = (unsigned int)seed;

    name_length = 6 + mrand(10);
    email_length = 10 + mrand(10);
    memo_length = 5 + mrand(10);

    num = mrand(10);
    for (idx = 0; idx < lastname_length[num]; idx++)
        name[idx] = lastname[num][idx];
    for (; idx < name_length; idx++) name[idx] = 'a' + mrand(26);
    name[idx] = 0;

    for (idx = 0; idx < memo_length; idx++) memo[idx] = 'a' + mrand(26);
    memo[idx] = 0;

    for (idx = 0; idx < email_length - 6; idx++) email[idx] = 'a' + mrand(26);
    email[idx++] = '@';
    email[idx++] = 'a' + mrand(26);
    email[idx++] = '.';
    email[idx++] = 'c';
    email[idx++] = 'o';
    email[idx++] = 'm';
    email[idx] = 0;

    idx = 0;
    number[idx++] = '0';
    number[idx++] = '1';
    number[idx++] = '0';
    for (; idx < 11; idx++) number[idx] = '0' + mrand(10);
    number[idx] = 0;

    idx = 0;
    birthday[idx++] = '1';
    birthday[idx++] = '9';
    num = mrand(100);
    birthday[idx++] = '0' + num / 10;
    birthday[idx++] = '0' + num % 10;
    num = 1 + mrand(12);
    birthday[idx++] = '0' + num / 10;
    birthday[idx++] = '0' + num % 10;
    num = 1 + mrand(30);
    birthday[idx++] = '0' + num / 10;
    birthday[idx++] = '0' + num % 10;
    birthday[idx] = 0;
}

static void cmd_init() {
    scanf("%d", &ScoreIdx);

    InitDB();
}

static void cmd_add() {
    int seed;
    scanf("%d", &seed);

    make_field(seed);

    Add(name, number, birthday, email, memo);
}

static void cmd_delete() {
    int field, check, result;
    char str[20];
    scanf("%d %s %d", &field, str, &check);
    if (field == 0 && check == 2 && strcmp(str, "jungce") == 0) {
        printf("debug\n");
    }
    result = Delete((FIELD)field, str);
    if (result != check) Score -= ScoreIdx;
}

static void cmd_change() {
    int field, changefield, check, result;
    char str[20], changestr[20];
    scanf("%d %s %d %s %d", &field, str, &changefield, changestr, &check);

    result = Change((FIELD)field, str, (FIELD)changefield, changestr);
    if (result != check) Score -= ScoreIdx;
}

static void cmd_search() {
    int field, returnfield, check;
    char str[20], checkstr[20];
    scanf("%d %s %d %s %d", &field, str, &returnfield, checkstr, &check);
    if (strcmp(str, "19520624") == 0 && returnfield == 4 && field == 2) {
        printf("debug");
    }
    RESULT result = Search((FIELD)field, str, (FIELD)returnfield);

    if (result.count != check ||
        (result.count == 1 && (strcmp(checkstr, result.str) != 0)))
        Score -= ScoreIdx;
}

static void run() {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int cmd;
        scanf("%d", &cmd);
        switch (cmd) {
            case CMD_INIT:
                cmd_init();
                break;
            case CMD_ADD:
                cmd_add();
                break;
            case CMD_DELETE:
                cmd_delete();
                break;
            case CMD_CHANGE:
                cmd_change();
                break;
            case CMD_SEARCH:
                cmd_search();
                break;
            default:
                break;
        }
    }
}

static void init() {
    Score = 1000;
    ScoreIdx = 1;
}

int main() {
    setbuf(stdout, NULL);
    freopen("../input.txt", "r", stdin);

    int T;
    scanf("%d", &T);

    int TotalScore = 0;
    for (int tc = 1; tc <= T; tc++) {
        if (tc == 15) {
            printf("debug");
        }
        init();

        run();

        if (Score < 0) Score = 0;

        TotalScore += Score;
        printf("#%d %d\n", tc, Score);
    }
    printf("TotalScore = %d\n", TotalScore);

    return 0;
}