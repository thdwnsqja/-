# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 여기에서부터 게임이 시작합니다.
label start:

    NARR """
    [[이 세상을 구원해 줄 용사여 나의 부름에 답하여 이 곳으로 소환되거라.]
    """

    NARR "내 머릿속에서 이상한 목소리가 들렸다.\n머릿속이 조용해지자 내가 있던 곳은 집이 아닌 처음 보는 공간이었다." with dissolve

    AL "용사여 잘 왔다. 이 몸은 다르한 대륙 서쪽에 있는 코노로 왕국의 왕 알리라고 하네"
    
    NARR "알리는 나한테 자기소개를한 뒤 질문을 한다."

    AL "용사여 너의 이름이 무엇이냐?"

    python:
        povname = renpy.input("나의 이름은?", length=32)
        povname = povname.strip()
        if not povname:
            povname = "김 한"
        USER = Character("[povname]")
    
    USER "저는 [povname] 입니다."
    NARR  " 나는 알리한테 자기소개를한다."
    AL "[povname](이)라.... 좋은 이름이구나 "
    NARR "나는 알리 한테 질문을 한다."
    USER "그보다 아까 다르한 대륙? 코노로? 라고 하셨는데 그게 뭔지 알려주실 수 있나요?"
    AL "이곳은 네가 있던 곳이 아닌 다른 세계다. "
    NARR "알리는 간단하게 설명을 해준다."
    USER "다른... 세계...? 그러면 제가 있던 세계로 돌아갈 방법은 있는 건가요?"
    AL "미안하지만 그거는 어려울거 같구나. 미안하다."
    USER "그러면 저를 여기로 소환한 이유가 무엇이죠?"
    NARR "나는 알리한테 다시 한번 질문을한다."
    AL "용사 [povname] 나를 도와 마왕을 죽여줄 수 있나?"
    USER "마왕...?"
    AL "만약 나를 도와 마왕을 죽여주면 네가 원하는 소원 한 가지를 들어주겠다."
    USER "죄송하지만.. 사람을 죽여본 적 없는 선량한 시민입니다."
    NARR "라고 말을 하자 알리의 옆에 있던 남자가 큰소리로 화를 내며 말을 한다."
    JAN "시끄럽도다! 너는 폐하께서 소환하신 용사다.\n잔말 말고 어서 가서 마왕의 목을 가져와 받쳐라!!!"
    AL "잔 조용히해라!"
    NARR "알리는 옆에 있는 남자의 이름을 부르고 조용히 하라고 하자 잔은 입을 다문다."
    JAN "하지만 폐하! 어서 용사한테 마왕을 죽이고 오라고 명령을 하셔야 됩니다!"
    NARR "잔의 말을 들은 나는 한순간 짜증이 올라와 잔을 '죽이고 싶다.'라는 생각이 들었다."
    NARR "그 순간 나의 시야에는 하나의 시스템 문구 창이 뜬다."
    SYSTEM "목표를 정했습니다."
    NARR "시스템은 목표를 알리와 잔을 가리켰다. 놀라고 있던 와중 창이 다시 뜬다."
    SYSTEM "발사하겠습니까?"
    NARR "라는 문구가 떴다."
    menu:
        "발사하겠습니까?"

        "발사":
            jump did_fire
        "취소":
            jump cancel_fire

label did_fire:
    USER "발... 사?"
    NARR "나는 창에 떠있는 문구를 읽자.\n내 왼쪽 눈에서 한 줄기의 [[레이저]가 알리와 잔을 향해 발사된다."
    NARR "그러자 가만히 서 있던 마튼이 보호막을 펼쳤지만,\n한발 빨랐던 [[레이저]가 알리와 잔을 관통한다."
    MA "뭐하는 짓이냐!!!"
    NARR "마튼이 소리지르자 문이 열린다."
    ALA "무슨 소란이냐!!"
    MA "알레아님!!"
    NARR "문을 열고 들어온 것은 내 또래의 여자였다."
    ALA "마튼! 방금 그건 무슨 소리인지 설명을 해주거라."
    NARR "마튼은 방금까지 있었던 이야기를 설명한다."
    NARR "설명을 들은 알레아는 나를 보며 말을 한다."
    ALA "그러면 여기 있는 자가 아버지를 죽였다는 건가?"
    MA "그렇습니다."
    ALA "병사들이여 여기 있는 용사를 왕족 살인죄로 감옥에 쳐넣어라!!"
    NARR "알레아의 말에 2명의 병사들이 나를 끌고 지하로 향한다."
    NARR "그렇게 나는 지하에 있는 감옥에 수감되었다."
    ETC "앞으로 이곳이 네가 살 곳이다."
    NARR "나를 감옥에 넣은 병사가 말을 한다.\n그리고 알레아는 나를 찾아와 내 앞으로 말을 한다."
    ALA "용사 김 한.. 아니 범죄자 김 한 아버지를 살해한 이유는 뭐지?"
    USER "그냥 실수였다고!"
    ALA "실수..?"
    USER "어 갑자기 내 눈에서 '발사하겠습니까?'라는 메시지가 떠서 나는 그걸 읽었을 뿐이야!"
    ALA "그런가.. 실수라.. 그래 알았다."
    NARR "알레아는 내 말을 듣고 일어 스며 말했다."
    ALA "김 한 네가 한 말이 사실이라고 해도 너는 왕을 살해한 범죄자다.\n그건 변하지 않는다. 그리고 형벌은 100년 나중에 또 오마"
    NARR "알레아는 지하를 나간다."
    NARR "그렇게 다음날.\n알레아가 나를 다시 찾아왔다."
    ALA "좋음 아침이야 김 한 감옥에서의 밤은 어땠어?"
    NARR "자고 있던 나는 알레아의 말에 잠에서 깬다."
    USER "습기 빼면 괜찮은 거 같은데? 그보다 오늘은 무슨 일로 왔지?"
    ALA "네가 어제 아버지를 죽인 바람에 나는 하루아침에 왕이 됐어"
    USER "그래? 그거 잘 됐네 그러면 왕이 된 기념으로 나 석방해 줄 수 있어?"
    ALA "바보 같은 소리하지마"
    USER "아쉽네"
    ALA "농담을 하는 거 보면 아직까지는 지낼만 한가 보네 그러면 나중에 다시 올게"
    NARR "그렇게 시간이 지나고 내가 감옥에 들어오고 10일 정도 지났을 때 감옥을 지키는 병사들이 급하게 지상으로 올라간다."
    "챕터1.마족의 나라"
    USER "다들 왜 저렇게 바쁜거야?"
    NARR "내 질문에 병사가 답을 한다."
    ETC "나도 모르지"
    USER "거짓말하지 말고 방금 병사랑 얘기했잖아?\n여기에서 썩어 가고 있는데 그 정도는 알려줄 수 있지 않아?"
    ETC "아마도 마물의 습격이겠지"
    USER "마물이 있구나"
    ETC "밖에 상황이 어떤지는 모르겠는데,\n여기에서 일하는 사람들 까지 가는 거 보면 보통 녀석이 아니라는 거지"
    USER "그렇구나.. 나도 그렇고 너도 그렇고 이게 뭐냐...."
    ETC "인생이 다 그렇지 너도 전 폐하를 죽이지 않았으면 여기에서 이러고 있지 않았을 테니까"
    USER "그치.."
    NARR "나는 옆에 있던 병사랑 얘기를 하면서 시간을 보내고 있었다.\n처음에는 아무런 말도 안 했는데 계속 있다 보니까 서로 잡다한 얘기를 하게 되었다."
    NARR "시간이 지나고 시끄러웠던 밖은 다시 조용해졌다.\n'드디어 끝났다'라는 생각을 하게 되었을 때 감옥으로 걸어오는 발소리가 들었다." 
    NARR "뚜벅 뚜벅 뚜벅 뚜벅 뚜벅 뚜벅 뚜벅 뚜벅초"
    NARR "발소리가 가까워지자 병사는 떨리는 목소리로 말을 한다."
    ETC "누.... 누구냐!! 머... 멈춰라!"
    NARR "멀어서 잘 안 보였는데, 가까이서 보니까 사람이라고 하기에는 사람이 아닌 다른 느낌의 무언가였다."
    NARR "내가 생각을 하고 있을 때 병사가 입을 열며 말했다."
    ETC "마.... 마족이.. 왜.. 여기에..!"
    NARR "감옥으로 온 마족이 말을 한다."
    ETC5 "이 몸의 이름은 마왕 디아블로다."
    NARR "병사 앞에 온 마족은 자기 자신을 마왕이라고 칭했다."
    ETC "마... 마왕 이라고? 여기에 온 이유가 뭐지?!"
    NARR "병사는 디아블로를 향해 검을 꺼내어 말했다."
    DAV "이번에는 살인의 목적으로 오지 않아서 다행으로 여겨라."
    NARR "디아블로는 살기를 내뿜자 병사는 그대로 주저앉았고"
    SYSTEM "표적을 정합니다."
    NARR "내 시야에는 시스템의 문구가 떴고, 표적은 디아블로로 향했다."
    SYSTEM "발사하겠습니까?"
    NARR "시스템이 문구가 뜨자 디아블로는 나를 뚫어져라 쳐다보고 있었다.\n디아블로를 본 순간 나는 발사라고 외쳤다."
    USER "ㅂ... 발사!!"
    NARR "나의 왼쪽눈에는 [[레이저]가 나갔고 디아블로의 몸을 관통했다."
    USER "죽은...건가?"
    NARR "배에 구멍이 뚫린 디아블로의 몸은 다시 재생이 되어 상처 하나 없이 완전하게 복구됐다."
    DAV "그래 이거구나 용사여"
    NARR "몸이 다시 재생된 디아블로는 나한테 말을 걸었다."
    DAV "용사여 방금 그 능력으로 왕을 죽인 거냐?"
    NARR "디아블로가 나한테 물어봤지만 나는 아무런 말도 안 했다."
    USER "....................................."
    DAV  "용사 다시 한번 묻겠다. 네가 이 나라의 왕을 죽인 것이냐?"
    NARR "디아블로가 다시 묻자 나는 답을 했다."
    USER "일단은... 그렇지?"
    NARR "그 말을 들은 디아블로는 웃는다.."
    DAV "하하하하!!!!!!!!!!!!"
    NARR "큰 소리로 웃은 디아블로는 나한테 한 가지의 질문을 했다."
    DAV "용사여 마족의 편에서 스지 않겠나?"
    NARR "황당한 질문을 받은 나는 어이없다는 표정으로 말을 한다."
    USER "나보고 지금 인간을 적으로 만들라는 거냐?"
    DAV "그렇다."
    USER "내가 너를 왜 도와줘야 되지?"
    DAV "이런 감옥에서 썩힐빠엔 나랑 같이 가는게 어때?"
    NARR "나는 디아블로 한테 물었다."
    USER "너랑 같이? 왜 하필 나지?"
    NARR "디아블로는 말을 이어 갔다."
    DAV "그러는 너는 여기에 평생 썩을 건가?"
    NARR "디아블로의 말에 나는 고민을 한 뒤 말을 했다."
    USER "여기보다는 너랑 같이 가는 게 좋을 거 같기도.. 하고?"
    NARR "내 말을 들은 디아블로는 웃으면서 말을 한다."
    DAV "후하하하하!! 좋은 선택을했다. 용사!!"
    NARR "디아블로는 쇠창살을 손으로 가볍게 부신 다음 손을 내밀었다."
    DAV "잡아라 지금부터 많이 바빠질 것이다."
    NARR "나는 디아블로의 손을 잡고 감옥 밖으로 나갔다."
    "성 밖"
    NARR "내가 본 밖의 환경은 싸움의 흔적은 있지만 사상자는 없었다."
    DAV "디아블로 : 그러면 가면서 이야기를 하지 [[소환술]!"
    NARR "디아블로는 소환술로 드래곤을 꺼냈다. 드래곤의 위에 올라탄 디아블로는 나한테 손을 내밀었다."
    NARR "내가 디아블로의 손을 잡으려고 하자 알레아가 멀리서 말을했다."
    ALA "[povname] 당장 마왕 한테서 떨어져!!"
    DAV "알리의 딸이군"
    ALA "마왕.... 갑자기 나타나서 무슨 짓이냐!! 전쟁이라도 하고 싶은 것이냐?!!"
    DAV "전쟁? 나는 원한다면 받아줄수있다. 하지만 지금 너의 나라의 상태를 보아라!!\n이 몸 한 명의 등장으로 거의 다 전멸이지 않냐? 잘 생각해라 코노로의 새로운 왕이여"
    NARR "디아블로는 알레아한테 충고를 하고 날아간다."
    "마족령 가는길"
    DAV "그래서 용사 이름이 뭐냐?"
    USER "[povname]"
    DAV "괜찮은 이름이군"
    NARR "나는 디아블로 한테 질문을 한다."
    USER "마왕님이라고 했나? 궁금한게 있어"
    DAV "편안하게 디아블로라고 해도 좋다. 궁금한 게 무엇이냐?"
    USER "이렇게 까지 해서 나를 구해준 이유가 뭐지?"
    NARR "나는 디아블로 한테 물고, 디아블로는 나의 질문에 답했다."
    DAV "나는 너의 힘을 빌려 교황이라는 자를 죽이려고 한다."
    USER "교황?"
    DAV "그렇다."
    USER "그거라면 너 혼자서도 되지 않아?"
    DAV "혼자서? 모른다. 하지만 질 확률이 더 크다. 그리고 교황은 한 명이 아니라 다른 대륙에도 있다.\n만약 그 녀석들까지 온다면 우리 마족은 단숨에 전멸할 것이다."
    NARR "디아블로는 한 명의 교황이 마왕을 능가할 힘을 가지고 있다고 했다.\n그렇기에 용사인 나를 코노로 왕국을 습격해서 나를 데려왔다고 했다."
    "마족령"
    DAV "도착했다. 용사"
    USER "편하게 [povname](이)라고 불러도 돼"
    DAV "알겠다."
    NARR "나는 디아블로의 뒤를 따라 마족령으로 들어갔다.\n마족령은 만화에서 나온 것처럼 괴상하지 않고, 인간들처럼 평범한 삶을 살고 있었다."
    NARR "디아블로가 돌아오자 2명의 마족들이 디아블로의 앞에 나타났다.\n두 마족의 이름은 자켄 이랑 아가레스 라고 하는 마족이었다."
    KEN "마왕님 다녀오셨습니까?"
    DAV "자켄 이구나 사냥이라고 한 건가? 고생했다."
    KEN "감사합니다."
    AGARES "그보다 마왕님 뒤에 있는 자는 누굽니까??"
    DAV "여기있는 자는 이번에 소환된 용사다. 코노로의 알리 왕을 죽인 녀석이고,\n교황과의 싸움에서 필요해서 데려왔다."
    NARR "그 말을 들은 아가레스랑 자켄 그리고 다른 마족들이 놀랐고, 아가레스는 놀란 말투로 말을 했다."
    AGARES "마....마왕님 그자는 용사입니다! 인간이라고요!\n아무리 인간의 왕을 죽였다 한들 경계도 안하고\n마족령에 데려오는 것은 아니지 않습니까?"
    DAV "그렇기는 하지 그런데 그런데 이 몸이 하겠다는데 불만이라도 있나 아가레스?"
    AGARES "아..... 아닙니다. 마왕님.."
    NARR "그렇게 디아블로는 나를 데리고 마왕의 성으로 들어갔다."
    "마왕의 성"
    DAV "[povname]이여 어떤가? 짐의 나라에 온 걸 환영한다."
    USER "내가 생각한 것보다는 괜찮은 것 같네.."
    DAV "그런가? 다행이구나 앞으로는 여기서 지낼 거니까 편하게 있어라"
    NARR "내가 마족령에 들어온지 3일이 지났을때 다른 마족들이 시위를 했다."
    AGARES "마왕님!! 지금 다른 마족들이 용사를 내쫓으라고 시위를 하고 있습니다."
    DAV "[povname]을(를) 말이냐?"
    AGARES "그... 그렇습니다."
    NARR "아가레스의 말을 들은 디아블로가 창문을 보자\n마족들은 내 이름을 적은 플래카드를 들고 시위를 하고 있었다."
    NARR "디아블로는 그 장면을 보고 나서 창문으로 점프했다.\n디아블로의 점프를 보고 놀란 나는 창밖을 내다보자 디아블로의 목소리가 위에서 들렸다."
    DAV "마족들이여!! 짐의 말을 잘 듣거라!! 언젠가는 교황이 우리를 공격하러 올것이다!! 나는 그것에 대비해 용사를 우리편으로 만들었다!! 이번 용사는 나랑 같이 교황을 죽이기로 약속을 한 사나이다!! 그것에 대해 무엇이 불만이냐!!"
    NARR "디아블로의 말이 끝나자 마족들은 화를 냈고 디아블로 앞에 한 명의 마족이 나타났다.\n그 마족의 이름은 무르무르였다."
    MU "마왕님 잘 생각해 보십쇼 용사라는 자가 우리를 배신해 마족들을 죽이고\n교황의 편에 서면 그때는 어떻게 하실 겁니까?"
    DAV "흠.. 그럴 수도 있구나.."
    USER "네가 설득을 당하면 어떡하냐!!"
    NARR "나는 큰소리로 말했고, 그 말을 들은 디아블로는 나를 한번 쳐다보고 다시 말을 했다."
    DAV "그러면 이렇게 하지 만약에 김 한이 우리를 배신하고\n교황의 편에서 스면 나는 그 즉시 다른 마왕들과 함께 이 세상을 멸망 시킬 것이다."
    ETC1 "디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로! 디아블로!"
    NARR "그 말은 평범한 인간이 내게는 말이 안 되는 소리 였지만\n시위를 하고 있던 마족들은 디아블로의 이름을 외치며 찬양하듯 말했다."
    NARR "그리고 그 광경을 본 무르무르가 다시 입을 열었다."
    MU "그렇게 까지 하실 필요는 없는 거 같습니다."
    DAV "그러면 더 좋은 방법이 있나?"
    MU "그렇습니다."
    NARR "디아블로는 무르무르의 말에 흥미가 생겼는지 어떤 방법인지 물어본다."
    MU "알겠습니다. 마왕님 용사 [povname] 이랑 영혼의 계약을 하는 게 어떻습니까?"
    DAV "영혼의 계약?"
    MU "그렇습니다. 만약 용사가 마왕님을 배신하면 용사의 심장이 멈추는 조건으로 하는 게 어떻습니까?"
    NARR  "무르무르가 말을 하자 다른 마족들은 아쉬워 하는 모습을 보였다.\n그리고 그 말을 들은 디아블로는 잠시 고민을 한 뒤 나를 불러 말을 했다."
    DAV "[povname]이여 자네한테는 미안하지만 여기에 지낼 거면 영혼의 계약을 하는 게 좋을 것 같구나"
    NARR "디아블로의 말이 끝나자 나는 질문을  했다."
    USER "디아블로 영혼의 계약이 뭔데?"
    NARR "나는 디아블로한테 영혼의 계약이 무엇 인지에 대해 물어봤다."
    MU "영혼의 계약이란 두 개의 영혼을 걸고 하는 계약 즉 인간들의 노예들한테 자주 쓰이는 계약이다.\n계약을 어길 시 그 자의 심장은 그 순간 멈춘다. 어떤가 용사여 하겠나?"
    NARR "대답은 디아블로 대신 무르무르가 말을 했고, 그 말을 들은 나는 고민을 하고 답을 했다."
    USER "그러면 그거 말고는 내가 하고 싶은 대로 하면 되는 거지?"
    MU "그렇다."
    DAV "너는 괜찮은 것이냐?"
    NARR "나는 망설임 하나 없이 바로 답을 했다."
    USER "여기가 아니면 살 곳도 없는데 어쩌겠어 영혼의 계약인지 뭔지 하자"
    MU "그러면 마왕님 계약을 시작하겠습니다."
    NARR "무르무르가 주문을 외우자 나랑 디아블로의 주위를 영혼들이 둘러쌓았다.\n그리고 시간이 지나자 영혼들이 사라졌다."
    USER "뭐야? 이게 끝이야?"
    DAV "그런거 같구나 그러면 이제 충분히 만족했나??"
    NARR "영혼의 계약이 완료되고 대부분의 마족들은 나를 경계하지 않았다."
    "그렇게 2개월이 지나고"
    NARR "나는 디아블로의 옆에서 마족들의 생활이나 하는 일 등을 보았다.\n내가 생각한 것처럼 나쁜 짓은커녕 평범하게 숲에서 몬스터를 잡아오거나 그 정도였다."
    NARR "저녁이 되고 자켄이랑 아가라스가 해수라는 몬스터를 잡아왔다."
    DAV "해수는 처음보나?"
    NARR "디아블로가 나한테 물었다."
    USER "해수가 뭐야?"
    DAV "바다에 사는 커다란 물고기 같은 거니까 먹어보면 좋아할 거다. 그러면 오늘은 밤은 파티다!!!!!!!!!!"
    NARR "그렇게 우리들은 해수 고기 파티를 하고 있던 와중 무르무르가 나한테 다가왔다."
    MU "용사여 마법을 배워보지 않겠나?"
    USER "마법..?"
    MU "그렇다. 내가 알려 줄 수 있는 건 간단한 암흑 계열 마법뿐이다."
    USER "암흑..마법? 나는 용사인데 빛의 마법이나 불의 마법 그런 거 배워야 되는 거 아니야?"
    MU "왜 그렇게 생각하지?"
    USER "아니 대부분의 용사들은 빛의 마법이나 막 그런 거 쓰지 않아?"
    MU "네 말이 맞지 근데 너는 특이 체질이다."
    USER "특이 체질..? [[레이저]면 빛의 마법 아니야??"
    MU "음.. 그렇게도 볼 수 있지만 사실 너는.."
    NARR "무르무르가 말을 하려는 순간 파티장에서 마족들의 환호 소리가 들렸다.\n무르무르랑 나는 환호 소리가 들린 곳으로 가보았다."
    NARR "그곳에서는 아가레스랑 디아블로의 팔씨름 장면이었다. 승자는 디아블로였다.\n팔씨름에서 이긴 디아블로는 나의 이름을 부르면서 말했다."
    DAV "어이!! [povname]!!! 너도 와서 팔씨름 한판해볼래?!"
    NARR "술을 마시고 취한 디아블로가 나한테 팔씨름을 하자고 권유했다."
    USER "어이 그건 아니지! 내가 너랑 팔씨름을 하면 내 팔은 그대로 아작 나는데 하겠냐?!"
    NARR "나는 바로 거절 했다."
    DAV "푸하하하!! 그래 나중에 꼭 하자꾸나!"
    NARR "나를 데리고 온 디아블로는 자신이 마왕이라는 존재가 아닌 한 명의 마족으로써 다른 마족들이랑 놀았다."
    "그렇게 다음날 디아블로의 방"
    USER "디아블로 그만 자고 일어나"
    DAV "으윽.. 어제 너무 많이 마셨네.."
    NARR "디아블로가 잠에서 깬 다음 말을 했다."
    DAV "여~ 어제는 잘 놀았냐?"
    USER "어제 니가 취해서 노래부르고 막 장난 아니었지"
    DAV "하하하!! 마음에 들었다면 다행이구나!"
    USER "나베리우스한테 들었어 이번 파티 나를 위해서 열었다고"
    DAV "나베리우스 이 녀석 쓸데없는 소리를.. 아무튼 나베리우스의 말대로 새로운 동료가 된 너를 축하하기 위해 연 파티였지"
    USER "하하 역시 너는 착한 마족인 거 같아"
    DAV "이 세상에는 착한 마족은 없다. 그리고 오늘 어디 좀 갈 거니깐 같이 가자."
    USER "어디 가는데?"
    DAV "가보면 알다 다른 애들도 같이 가니까 바로 갈 준비해줘"
    USER "알았어"
    "그렇게 다 모이고"
    KEN "다 모인 건가?"
    NABE "그런 거 같군"
    DAV "그러면 가자"
    "전쟁의 시작"
    NARR "우리는 디아블로를 따라서 지하 깊은 곳으로 들어갔다."
    NARR "가는 길에는 다른 애들이 아무런 말없이 조용히 디아블로의 뒤를 따라갔기 때문에\n나는 아무 말 없이 그 들을 따라 갔다."
    NARR "그렇게 우리가 도착한 곳은 큰 문이 있는 곳이었다.\n문 앞에 도착한 디아블로는 가만히 멈춰 선 다음 입을 열었다."
    DAV "들어가기 전에 몇 가지 약속을 해줘"
    USER "약속?"
    DAV "어"
    USER "그 정도야 간단하지"
    DAV "그냥 친구들끼리 약속하는 거니깐 크게 걱정할 필 요는 없어"
    USER "알았어"
    DAV "첫째. 방 안에서 있었던 일은 아무한테나 말하지 말 것\n둘째. 밖에서 문을 열기 전까지 문을 열지 말 것 \n셋째. 도망치지 말 것 그리고 마지막으로 넷째 꼭 살아서 돌아와라"
    USER "?? 살아서 돌아오라니?? 그게 무슨뜻인데?"
    NARR "디아블로는 문을 열고 나를 방 안으로 밀쳤다."
    "방안"
    USER "어이!!!! 야 인마!!! 뭐 하는 짓이야!!!"
    NARR "나는 문을 두드리며 큰소리로 소리를 질렀지만 아무런 대답이 없었다.\n그리고 나는 마음속을 진정 시키고 주위를 둘러보면서 말했다."
    USER "뭐 하는 곳이길래 그러지.. 그보다 너무 한거 아니냐 이렇게 어두운 곳에 보내다니"
    NARR "나의 말이 끝나자 어두웠던 방 안에 있던 등불이 켜지자 내 앞에 있던 건 한 명의 마족이었다. 그 마족의 외형이 디아블로와 닮은 외형의 여자였다."
    USER "디아블..로? 는... 아닌데..? 누구세요??"
    ETC5 "이 곳에 인간 이라니.. 참 이상한 짓을 하네.."
    LIL "소개하지 나는 릴리스라고 하네"
    USER "릴리스?"
    LIL "디아블로의 누나야"
    USER "디아블로의 누나?!!"
    LIL "놀랐어?"
    USER "앗.. 네! 처음 뵙겠습니다."
    NARR "릴리스는 웃으면서 말한다." 
    LIL "후훗 편하게 해~"
    USER "네.."
    LIL "아무것도 모르고 온거지?"
    USER "네.."
    LIL "그러면 설명해 줄게 여기는 내가 살고 있는 다른 차원이라고 보면 돼"
    USER "다른 차워..?"
    LIL "자세한거는 넘어갈게"
    USER "네.."
    LIL "디아블로는 잘 지내?"
    USER "조금 같이 지내 본 결과 자신의 방법대로 다른 마족들을 잘 이끌어 나가고 있어요"
    LIL "그래? 다행이네"
    USER "그리고 이번에 제가 왔다고 다른 마족들이랑 같이 파티 준비를 해줬어요"
    LIL "나쁜길로 안 빠져들어서 다행이네.."
    NARR "릴리스는 잠시 생각을 한 뒤 말을 한다."
    LIL "이제 본론으로 넘어가서 인간치고는 강력한 마력을 지니고 있네?"
    USER "마력이라는게 보여요?"
    LIL "물론~ 평범한 마족들은 조금만 수련하면 보인고, 인간들 중에서도 보는 인간들도있고"
    USER "그렇구나.."
    LIL "마력을 보아하니 용사구나"
    USER "어떻게 아셨어요?"
    LIL "그렇게 거대한 마력을 가지고 있으면 누구든지 다 알아"
    USER "대단하시네요"
    LIL "그런데 그 용사가 왜 마족령에 있지?"
    USER "실수로 코노로 왕을 죽여서 감옥에 갇혔는데,\n디아블로가 도와줘서 여기에 살고 있어요"
    LIL "벌써 부터 꼬였구나.."
    USER "뭐가 꼬인거죠??"
    LIL "디아블로가 이 곳으로 아무 말 없이 데려왔다고 했지"
    USER "네"
    LIL "이런 중요한 것도 알려주지 않고.... 바보구나.."
    NARR "나는 릴리스의 말에 침묵을 했고 릴리스는 말을 계속했다."
    LIL "일단 몇가지 알려줄게 너는 용사야 그치?"
    USER "그렇죠?"
    LIL "그리고 너의 주 마법은 어둠 마법이 될 거야 알았지?"
    USER "어둠 마법 이요..?"
    LIL "일단 너는 어둠 마법을 쓰는 게 효율이 좋아 보이거든"
    USER "그러면 제가 가지고 있는 능력은 어둠 마법쪽인 거에요?"
    LIL "너의 능력이 뭔데? 보여줄 수 있어?"
    USER "보여주기에는.. 발동 조건을 몰라서.."
    LIL "발동 조건이라... 그러면 이건 어때?"
    NARR "릴리스가 말을 끝나자 오크가 나타났다."
    USER "어디서 나온거죠??"
    LIL "그냥 간단하게 소환 한거야 그러면 너는 이제 오크가 너를 죽이려고 공격을하고 너는 능력으로 살아 남아봐"
    USER "죽인다고요?!!"
    NARR "나의 말이 끝나자 오크는 나를 향해 공격하기 시작했고\n순식간에 내 눈앞으로 이동한 오크는 도끼로 나를 찍었다."
    USER "끄아아아악!!!! 아파!!!!!!!!"
    LIL "흐음..."
    NARR "도끼에 찍히자 나의 시야에는 시스템의 문구가 떴다."
    SYSTEM "[[표적을 정합니다.]"
    SYSTEM "[[발사하시겠습니까?]"
    USER "ㅂ... 발사!!!!"
    NARR "발사라고 외치자 나의 왼쪽 눈에서 한줄기의 레이저가 나가고 오크의 몸을 관통했다."
    LIL "이거구나.."
    NARR "릴리스는 감탄하듯 말을 한다."
    USER " 하아... 하아.."
    NARR "오크가 쓰러지자 나도 몸에 힘이 풀려 잘린 팔을 부여잡고 그대로 드러누웠다."
    LIL "괜찮네..."
    NARR "릴리스가 내 쪽으로 걸어오며 말을 한다."
    LIL "꽤 괜찮은 능력이네"
    USER "칭찬인가요? 저는 방금 죽을 뻔했는데.."
    LIL "이런 걸로 죽으면 안되지"
    USER "그러면 지금 당장 죽기 일보 직전 이니까 회복은 없나요?"
    LIL "그 정도는 해줄게"
    NARR "릴리스가 상처 난 부위에 손을 대자 상처가 회복된다."
    USER "이게.. 회복 마법..? 대단하네.."
    LIL "인간들이 쓰는 회복 마법이야 이제 괜찮지?"
    USER "네"
    LIL "오크를 이기는 거는 잘했는데 아직 많이 부족하네 이대로 가다간 금방 죽겠어"
    USER "평범하게 살면 되지 않을까요?"
    LIL "평범? 이곳에 와서 평범하게? 그렇게 해줄 수 있지 너는 평범하게 살고 싶니?"
    USER "이미 왕을 죽인 몸이라 평범하게는 못살 거 같네요"
    LIL "그치 그러면 모든 일이 끝날 때까지는 평범하게 못 살 거야"
    USER "하하하.."
    NARR "릴리스의 말에 나는 헛 웃음을 한다."
    USER "그러면 저는 이제 무엇을 하면 되나요?"
    LIL "어떻게 하고 싶어?"
    USER "어떻게 하고 싶다뇨?"
    LIL "나의 제자가 되는건 어때?"
    USER "제자 말인가요?"
    LIL "어"
    USER "어차피 여기 있는 동안 아무것도 못하니까 한번 해볼게요"
    LIL "좋아 합격이다!! 디아블로가 너를 보낸 이유도 너를 강하게 만들려고 데려온거 같은데, 내가 너의 스승이 되어주지"
    USER "스승이요?"
    LIL "그렇다. 내가 너를 강하게 만들어 주마 다만, 죽을 정도로 힘들다는 것은 알고 있어라."
    USER "........"
    LIL "일단 너의 능력인 [[레이저]는 김 한 네가 생명에 위협을 받거나 아니면 상대를 적으로 간주했을 때 발동할 수 있는 것 같아"
    USER "상대를 적으로 간주?"
    LIL "어"
    USER "그거를 알 수 있나요?"
    LIL "아까 네 몸에 손을 댔을 때 잠깐 확인해봤지\n그런데 여러 가지 조건이 있어서 지금은 그 성능을 다 못 쓸 거야"
    USER "잠깐 확인한 걸로 그 정도가 되면 스승님은 대단한 마족인가요?"
    LIL "나는 원래 대단해서 이 정도는 별거 아니지 그러면 지금부터 교육을 시작할게"
    NARR "그렇게 릴리스의 교육이 시작되었다."
    "한 편 문 밖"
    DAV "대화를 들어보니 오래 걸리겠네 너희들도 각자 수련을 하도록 해 교황이 언제 쳐들어 올지 모르니깐"
    "내가 지하에 있는 방에 들어오고 며칠이 지났다."
    USER "스승님?"
    LIL "왜?"
    USER "며칠 동안 여기서 배운 건 알아듣지 못하는 언어인데 맞아요?"
    LIL "알아듣지 못한 거라니 엄연히 마족어라고"
    USER "그게 문제인거죠!!!"
    LIL "네가 그렇게 화내는 이유도 알고 있다. 참고 견뎌 네가 선택한 길이다. "
    USER "으아아아아아아아아!!!!!!"
    "그 시각 어느 나라"
    ETC6 "교황님  다른 종족들과의 연합이 완성되었네요"
    G "그렇다고 하네요 비륵"
    BA "시기는 언제로 하실 건가요?"
    G "저쪽도 슬슬 준비를 하고 있겠지요.\n지금부터 3주 뒤 저희 연합은 마족령을 습격할 겁니다."
    BA "알겠습니다. 그러면 바로 갈 수 있게 준비를 할게요"
    "다시 마족령"
    DAV "김 한이 얼마나 강해질지는 모르겠지만.. 그를 믿어보자"
    KEN "용사가 마법 쪽이어서 다행이네요 만약 검이나 격투가였으면 큰일이죠"
    DAV "그런가.."
    NABE "디아블로님 방금 들린 정보로는 교황이 3주 뒤에 습격을 한다고 했습니다."
    DAV "꽤 빠르군"
    MU "언제 공격해와도 저희들은 해낼 겁니다."
    AGARES "당연한 소리를!"
    DAV "무르무르"
    MU "넵"
    DAV "지금부터 인간이 공격하기 전까지 너는 시체 군단을 더 강화 시켜라"
    MU "알겠습니다."
    DAV "그리고 나베리우스"
    NABE "부르셨습니까?"
    DAV "너는 마족령 주위에 잠들어있는 가고일들을 깨워서 대기 시키고\n아가레스, 자켄 은 만일을 대비해 도망칠 공간을 만들어 놔라"
    KEN "왜 그런 건 저희한테 시키시는 겁니까"
    DAV "미래를 위해서다."
    AGARES "잔말말고 따라와 자켄"
    NARR "아가레스가 자켄을 끌고 간다."
    KEN "으아아아!!"
    "그렇게 2주뒤 방 안"
    USER "스승님"
    LIL "왜그러지?"
    USER "이렇게 놀고만 있어도 되는 거예요?"
    LIL "쉬는 것도 중요하단다."
    USER "더 강력한 마법을 알려 줘야 하는 거 아니에요?"
    LIL "나도 마음 같아서는 내가 가지고 있는 지식을 다 알려주고 싶은데,\n너는 아직 그걸 감당할 그릇이 안 된다."
    USER "스승님이랑 디아블로가 그렇게 강하면 두 분의 부모님은 얼마나 강한 거예요?"
    LIL "얼마나 강했냐면..."
    USER "두구두구두구두구두구"
    LIL "솔직히 나도 잘 몰라"
    USER "모른다뇨?!! 그게 말이 되나요??"
    LIL "그게 본 적이 없거든."
    USER "그게 무슨..!!"
    LIL "나랑 디아블로는 사천왕이 키웠지"
    USER "사천왕?"
    LIL "어라..? 본적없어? 그 왜 디아블로의 옆에 다니는 4명 있잖아."
    USER "그 녀석들이 사천왕이었어요??"
    LIL "얘네는 무슨 그런 거 하나도 안 알려주냐...."
    USER "걔네들도 사정이 있으니깐 그런 거지 않을까 싶네요."
    LIL "뭐 그렇겠지"
    USER "언제쯤 나가냐...."
    LIL "나가고 싶어?"
    USER "밖에 상황이 궁금해서요"
    LIL "괜찮을거야"
    USER "그리고 나가고 싶어도 문을 열어줄 때까지 열지 말고 있으라고 해서 마음대로 못 열죠"
    LIL "그 말은 너의 수련이 가장 중요하다는 거네"
    USER "교황이라는 자가 얼마나 강하면...."
    LIL "강하긴 하지"
    USER "교황을 알고 있나요?"
    LIL "내가 이곳에 오기 전에 잠깐 본 적 있는데 강한 인간이었지"
    USER "스승님께서도 그렇게 말하다니.. 만약에 교황이랑 스승님이랑 싸우면 누가 이겨요?"
    LIL "그런 쓸데없는 질문을 하다니 지금부터 다시 훈련이다."
    USER "에에에..."
    LIL "나랑 교황이랑 싸우면 누가 이기는지 궁금하다고 했지?\n싸워보지 않아서 모르겠는데 비등할거야"
    USER "그렇게 말해도 잘 모르겠네요"
    LIL "어찌 됐든 다시 훈련 시작이다."
    "그렇게 1주일 뒤 마족령"
    KEN "마왕님! 인간들이 나타났습니다!!!"
    DAV "예상보다는 조금 빠르군... 자켄 내가 말한 건 준비됐지?"
    KEN "네.. 작은 주머니 안에 넣어서 가져왔습니다."
    DAV "잘했다. 나는 김 한을 데려올 테니 잠시 상대 좀 해줘\n교황이 먼저 나타나거나 너 혼자 안될 거 같으면 당장 후퇴해라"
    KEN "알겠습니다!!"
    "한편 교황쪽"
    G "이번 전쟁에서 승리해야만 세계의 평화가 찾아옵니다!!!\n마족들을 한 마리도 남김없이 해치 버린 다음, 이 땅에서 완전히 멸망시키는 겁니다!!"
    ETC7 "오오오오!!!!!!!!!!!!!!!!!!!!!!! 가즈아!!!!!!!!!!!!!"
    "그 시각 [povname]쪽"
    LIL "제자여"
    USER "갑자기 안 하던 말투를...."
    LIL "시끄럽고 이제 때가 된 것 같구나"
    USER "때가 됐다는 게...."
    LIL "우리가 헤어질 때가 된 거지"
    USER "그렇게 말하면 차이는 느낌이 나는데...?"
    LIL "장난치지 말거라. 하지만 그런 너한테 부탁을 해도 되나?"
    USER "부탁이요?"
    LIL "그리 어렵지 않은 거야"
    USER "어떤 거예요?"
    LIL "시간이 남고 그러면 여기서 나를 해방해줄 수 있나?"
    USER "해방이요?"
    LIL "그렇다."
    USER "해방하면 못 보는 거 아닌가요?"
    LIL "아 여기 처음 올 때 다른 차원이라고 했지?\n사실 여기는 나를 봉인 하기 위해 만든 다른 차원이야."
    USER "스승님을 봉인?"
    LIL "그렇다. 어렸을 때 내 힘이 불안정하고 언제 폭주할지 몰라서\n내 스스로 날 봉인 해달라고 부탁했어"
    USER "풀려면 어떻게 해야 하나요?"
    LIL "그건 나중에 알려줄게"
    USER "네"
    LIL "그리고 디아블로가 어떤 선택을 하더라도 너는 디아블로를 믿는 거야 알았지?"
    USER "당연하죠!"
    LIL "좋아! 그럼 가봐 문이 열렸다."
    USER "문이요..?"
    NARR "릴리스의 말에 뒤를 돌아보자 밖에서 빛이 조금씩 들어오기 시작했다."
    LIL "그러면 나중에 보자꾸나"
    NARR "릴리스의 말이 끝나고 나는 방에서 나왔다."
    LIL "그러면 건강하거라. 나의 제자여..."
    "문 밖"
    DAV "여~ 김 한 그동안 많이 성장했나?"
    NARR "내가 방에서 나오자 디아블로가 나를 반겨줬다."
    USER "모르겠네"
    DAV "고민이라도있나??"
    USER "방 안에 있었던 일들을 말하지 말라고 해서 못하는 게 아쉬워서"
    DAV "그런가! 아쉽군!"
    USER "많이 배우지 못했는데 괜찮겠어?"
    DAV "그렇다. 나는 너를 믿고 있는다. 그리고 전쟁이 시작되었다."
    USER "전쟁?"
    DAV "그렇다. 조금 전에 교황이 우리 진형을 쳐들어왔다."
    USER "나오자 마자 전쟁이라니!"
    DAV "무서운가??"
    USER "당연히 무섭지!! 잘못하다가 죽을 수도 있잖아!!"
    DAV "하하하!"
    USER "이 상황에 웃음이 나오냐!!"
    DAV "나는 알고 있었다. 오늘 교황이 쳐들어오는 것도"
    USER "그러면 왜 말 안 해줬어?!!"
    NARR "디아블로에게 큰 소리로 얘기하자 디아블로는 진지한 표정으로 말을 했다."
    DAV "진정하고 들으라고 내가들어라 내가 미리 말을 한다고 해도 달라지는 건 아무것도 없다."
    USER "그러면 만약 처음에 내가 너를 안 따라갔으면 나는 지금쯤 어떻게 됐지?"
    DAV "아마도 교황의 손에 죽었을거다."
    USER "하하하...."
    DAV "무서운가? 그러면 지금 이라도 도망치게 해줄까?"
    USER "내가 도망쳐도 어차피 교황은 날 노리잖아"
    DAV "그렇지."
    USER "도망쳐도 죽을 바엔 같이 싸우다가 죽는 게 낫지"
    DAV "하하하!! 좋은 선택이다!! [povname]!! 그러면 출발하도록 하지!!"
    "그렇게 전장"
    NABE "오셨습니까? 마왕님"
    DAV "그래 나베리우스 나 대신 고생 많았어."
    NABE "아닙니다."
    USER "오랜만에 밖에 나오네"
    NABE "건강해 보이네? 잘 있었나?"
    USER "그렇게 보이는구나"
    NABE "당연하지, 아니면 무슨 문제라도 있나?"
    USER "밖에 나오자마자 전쟁한다는 소리를 들어서 많이 놀랐지"
    NABE "그런가 용케도 왔구나"
    NARR "디아블로는 나랑 나베리우스의 얘기를 끊고 말했다."
    DAV "작전이다. 나랑 김 한은 아가레스랑 자켄을 도와서 싸운다.\n그리고 나베리우스 너는 여기서 지휘 겸 후방지원을 부탁하마"
    NABE "알겠습니다. 마왕님!"
    NARR "나랑 디아블로는 날아가 전방으로 갔다."
    KEN "꽤 일찍 왔네? 늦잠 자고 와도 되는데?"
    USER "푹 자고 와서 괜찮거든?"
    KEN "하하하! 그거참 다행이네!"
    DAV "자켄 아가레스는?"
    KEN "아가레스는 앞에서 싸우고 있습니다."
    DAV "알았다. 그러면 시작해볼까?"
    USER "좋아!!!!!!!!"
    DAV "그러면 [povname] 멋지게 시작해보거라"
    USER "내가?!!"
    DAV "당연하지"
    USER "알았어"
    NARR "나는 숨을 들이마시고선 하늘 높이 날아갔다."
    KEN "거기서 뭐 하게 표적이 되고 싶어서 그러냐?"
    USER "적이라...."
    NARR "인간들 진형을 내려보자 하나의 붉은색 점이 보이고 시스템의 문구가 떴다."
    SYSTEM "[[표적을 정했습니다.]"
    USER "[[목표는 다수]"
    SYSTEM "[[지금부터 능력[[레이저]에 목표를 다수로 정합니다.]"
    NARR "시스템의 문구가 뜨자 나의 시야에는 수많은 붉은색 점들이 보였다."
    SYSTEM "[[발사하겠습니까?]"
    NARR "나는 숨을 크게 들이마시고 말을 한다."
    USER "발사"
    NARR "“발사”라고 말을 하자 왼쪽 눈에는 한줄기의 레이저가 나갔다.\n한줄기의 레이저는 수만 개의 줄기로 흩어지고 지상에 있는 적을 향해 날아갔다."
    AGARES "우왓?!!!"
    USER "아가레스 괜찮아??"
    AGARES "[povname] 방금 네가 한 거야??"
    USER "아가레스? 앞에 있던 거 아니었어? 왜 돌아왔어?"
    AGARES "왜 돌아오긴!! 방금 그거 네가 한 거지? 맞는 줄 알고 뒤로 뺐다!"
    USER "미안하게 됐어"
    AGARES " 다음부터 조심해!"
    USER "미안 미안 조심할게"
    DAV "대단하구나! 이 정도까지 성장할 줄은 몰랐다."
    USER "나도 이 정도의 수는 처음 해봤는데 되네....."
    DAV "좋다!! 지금이 좋은 타이밍 같구나!! 이 상태로 전진하자!!"
    KEN "알겠습니다!!!"
    NARR "나의 공격 한방으로 마족들의 사기가 올랐다."
    "한편 교황쪽"
    ETC "방금 그건 뭐지...?"
    G "당황하지 말거라! 방금 레이저는 코노로왕을 죽인 용사의 능력이다!"
    BA "교황님"
    G "바륵? 무슨 일이지?"
    BA "다간 한테서 온 내용입니다."
    G "무슨 내용이지?"
    BA "현재 아가레스랑 자켄의 협공으로 인해 진형이 무너지고 있다고 합니다."
    G "미천한 마족 녀석들!!! 대사제 지금부터 그 녀석을 꺼내야 할 때다 온 것 같군요."
    BA "비장의 카드 아니였나요?"
    G "자켄이랑 아가레스가 있는 상황에서 둘다 잡으려면 지금뿐입니다."
    BA "알겠습니다. 바로 데려 오겠습니다."
    "마족 진형"
    USER "뭐지.. 마력이 한쪽으로 모이고 있어.."
    DAV "마력도 볼 수 있나?"
    USER "배웠거든"
    DAV "좋다!! 아무래도 저 마법은 소환마법인 것 같군."
    USER "소환마법이 저런식으로 되는구나...."
    DAV "네가 소환되었을 때도 저렇게 요란스러웠지"
    USER "요란스럽다니"
    DAV "너도 배울래?"
    USER "나도 배울 수 있어?"
    DAV "이 몸이 가르쳐 주면 갓난 아기라도 금방 할 수 있지"
    USER "진짜로? 나중에 알려줘"
    DAV "하하하! 좋다! 알려주마!"
    NARR "그렇게 디아블로랑 잡담하고 있는 사이 소환마법이 끝났다."
    "인간 진형"
    ETC "새로운 용사의 소환이다!!!"
    G "마족들을 없앨 빛의 용사가 이 자리에 나타났다! 지금이야말로 우리의 힘을 보여줄 때다!!"
    "빛의 용사가 소환되고 인간연합의 행동에 망설임이 없어졌다."
    G "빛의 용사 재운이여 그동안 괜찮았나?"
    J "뭐.. 그렇저럭? 그 보다 진짜 저 녀석들 쓸어버리면 원래 세계로 돌려보내 주는 거지?"
    G "그렇다. 아니면 네가 여기서 원하는 삶도 가능하다."
    J "나는 한시라도 빨리 돌아가고 싶다고 여기에 있을 이유가 없거든."
    G "그러면 날뛰고 와라! [[신의 축복]"
    "교황이 [[신의 축복]으로 인간 연합의 능력이가 올라갔다."
    J "그러면 어디 한번 놀아볼까??[[빛의 검기]"
    "재운이 [[빛의 검기]를 날리자 전방에 있던 마족들이 사라졌다."
    "마족 진형"
    AGARES "이 마력... 심상치 않네..."
    KEN "그러게 말이다. [povname](이)랑 비슷한 마력이야 저 녀석도 용사인가??"
    AGARES "용사든 뭐든 다 날려버리면 그만이야"
    "자켄이랑 아가레스가 이야기하고 있는 동안 재운이 앞으로 날아 온다."
    J "너희가 교황이 말했던 녀석들이야?"
    KEN "빠르다..."
    AGARES "그러면 우리도 하나만 묻자 너는 용사인가??"
    J "그렇다고 하면?"
    AGARES "여기서 죽인다!!"
    "아가레스가 재운을 날려버린다."
    J "크윽.. 사람이 말을 하는데.. 비겁하네.."
    AGARES "아 그러셔? 그런데 나는 사람이 아니여서 말이지!"
    "아가레스가 재운을 땅에 꽃는다."
    "콰아아아앙!!"
    AGARES "지금이다!! 자켄!!"
    "아가레스의 말이 끝나자 자켄이 날아가서 재운의 머리를 내려 찍는다."
    "콰지직!!!"
    J "하찮은 마족들이!!!!"
    AGARES "그러면 하찮은 마족한테 죽어봐라."
    "재운이 일어나자 아가레스가 앞에 나타난다."
    J " !!!!! 어서.. 도망을..!"
    "재운이 도망치려고 하자 발이 안 움직인다."
    AGARES "도망? 나한테서 도망을 간다고? 어림도 없는 소릴"
    J "무슨 짓을 한 거야!!!"
    AGARES "우리의 능력도 모르면서 싸우려고한거냐? 한참 멀었군 그러면 이만 끝내지 지금이다. [povname]!!!"
    USER "발사!"
    "한줄기의 레이저가 재운을 향해 날아간다."
    J "!!!!!!!!!!!!!!!!!!!!!!!!"
    "레이저가 재운의 바로 앞에서 레이저가 사라진다."
    USER "무슨 일이지..?"
    BA "빛의 용사 기대했는데, 고작 이정도 인가요??"
    J "대 사제??"
    AGARES "대 사제 라고??"
    BA "여기에서 꾸물거릴 시간 없어요"
    NARR "바륵이 손짓을 하자 재운의 상처가 없어진다."
    AGARES "대 사제는 처음 상대 하는군"
    "우리는 바륵의 압박에 의해 움직이지 못했다."
    BA "어둠의 용사 [povname] 능력을 사용하는거면 그만 두는게 좋을거에요"
    "바륵의 말이 끝나자 나의 목 앞에 칼 한 자루가 떠다니고 있었다."
    USER "우왓!!"
    BA "그러면 빛의 용사는 뒤에서 지켜보기나 하세요."
    J "무슨 소리야!!! 여기서 저 녀석들을 죽여야지!!"
    BA "금 제 말의 뜻을 못 알아들은 건가요? 알아들을 수 있게 다시 말할게요. 당신은 쓸모가 없다고요."
    J "크윽..."
    AGARES "미안하지만 내 능력으로 도망 못가는건 잊이 않았지?"
    BA "아가레스 당신의 능력은 거슬리네요."
    AGARES "나에 대해서 아는 말투네"
    BA "모르면 이상하죠"
    AGARES "하하하하!!! 그치! 모르면 이상하지!!"
    KEN "어이! 지금 잡담할 때야?!!"
    AGARES "성질 한번 급하네 얘기는 나중에 하는걸로 하자"
    BA "살아 있기만 하면 언제든지 환영이죠"
    AGARES "적이지만 마음에 드는군 그러면 진심으로 상대해 주지"
    BA "빛의 용사는 배신자를 잡아 오도록 하세요"
    J "네~ 네~ 알겠어요~"
    KEN "방심하지 말라 저렇게 보여도 대사제니깐"
    AGARES "당연하지!!"
    BA "늦게 가면 교황님이 뭐라고 하니깐 금방 끝내 드릴게요."
    AGARES "어디 한번 덤벼 봐라!!"
    "한편 [povname] 쪽"
    J "왜 인간들을 배신 했지?"
    USER "나한테도 사정이 있다."
    J "사정?"
    USER "그렇다. 나는 인간의 왕을 죽여서 인간들에게 쫓겨 사는 것 보다\n마족들의 편에 서는 게 더 좋다는 생각했거든"
    J "그래?? 그러면 다시 돌아 올 생각은 없는 거지??"
    USER "거절하지"
    J "아쉽군 그래.."
    USER "뭐가 아쉽지?"
    J "교황이 그랬거든 만약 여기서 너랑 마왕을 죽여서 데려오면 집에 보내준다고 했거든."
    USER "집에 보내준다라.."
    J "너는 돌아가고 싶지 않아??"
    USER "나는 돌아가야만 하는 이유고 없어서 여기가 좋아"
    J "아쉽네 마음만 잘 맞으면 부탁해서 살려는 줄 생각이었는데"
    USER "어차피 살려줄 마음도 없었으면서 그러네"
    J "들켰네, 그러면 마지막으로 질문 하나 하자 이 전쟁에서 이기면 무엇을 하고 싶지?"
    USER "그냥 평범하게 살 생각이다."
    J "평범하게라.."
    USER "그런 의미에서 가주면 안될까?"
    J "나는 집에 돌아가고 싶어서 그거는 안 될 거 같아.\n그보다 교황 녀석 만만치 않아서 그냥 돌아가면 내가 죽거든."
    USER "그 녀석이 그 정도로 강해?"
    J "뭐 보면 알거야"
    NARR "나랑 재운이 얘기를 하고있는데, 밑에서 바륵이 재운을 불렀다."
    BA "빛의용사!! 잡담 그만 하고 어서 죽이기나 하세요!"
    NARR "땅을 내려 보자 쓰러져있는 자켄이랑 아가레스가 보였다."
    J   "뭐야? 벌써 끝난거야?"
    BA "당신도 어서 끝내고 돌아갈 생각을 해요"
    J "네~ 네~ 하여간 저 양반도 정상은 아니지"
    USER "자켄!! 아가레스!!"
    J "지금 동료들을 걱정하는건가?"
    USER "죽은거 아니지? 정신차려!!"
    BA "흠.. 위에서 뭐라고 소리를 지르는데요?"
    NARR "바륵은 쓰러져있는 자켄과 아가레스한테 말을 걸었다."
    KEN "크윽... 시끄러!"
    USER "내가 곧 내려 갈게! 기다려!"
    J "한 가지 알려주자면 대사제보다는 내가 더 싸우기 편할 거야"
    USER "누가 더 강한지는 상관 없어 어차피 다 이기면 그만이니까 잔말 말고 덤벼라"
    J "덤비라는데.. 들어가 줘야지!!!!!"
    NARR "그렇게 나와 재운의 싸움이 시작된지 몇십분이 지났다."
    J "레이저만 쓸 수 있다고 들었는데 아닌가 보네"
    BA "너무 늦게 끝나는데.. 그냥 제가 죽여 버려도 되나요?"
    AGARES "여기서 우리가 죽으면 마왕님을 볼 자격이 없지..!"
    NARR "아가레스가 일어 나려고 한다."
    BA "흠.. 발악인가요? 당신들이 아무리 발악해도 이 전쟁은 이길 수 없어요."
    AGARES "그거는 아무도 모르지!!"
    "디아블로 쪽"
    DAV "아가레스의 마력이 요동친다."
    NABE "이거 이거.. 큰일이군요.. 도와주러 갈까요?"
    DAV "아니 그럴 필요 없다. 나베리우스, 무르무르 한테 전해라. 강령술을 준비하라고 전해라"
    NABE "알겠습니다."
    DAV "봐주지 않을 생각인가보네.."
    "아가레스 쪽"
    USER "뭐야... 마력의 흐름이... 바뀌고있어.."
    AGARES "[[욕망이여 나의 모든 것을 먹어 치워버려라.]"
    NARR "아가레스가 주문을 외우자\n아가레스의 마력의 흐름이 빨라지면서 아가레스의 모습이 변한다."
    BA "변신...?"
    AGARES "이 모습은 모르는 모양이군"
    BA "역시 마족들은 괴물이군요.."
    AGARES "괴물이면 죽이게?"
    BA "!! 어느새 뒤에.."
    NARR "아가레스는 말이 끝나자 바륵의 뒤로 이동했다."
    AGARES "이 형태는 오랜만이어서 힘 조절 안 되니까 알아둬라."
    BA "어차피 하찮은 마족!! 지금부터는 봐주지 않겠다!!"
    NARR "아가레스와 바륵의 치열한 싸움이 시작되었다."
    USER "우리도 마저 해야지?"
    J "미안하지만 우리는 여기까지다."
    USER "얌마!!"
    NARR "재운은 나를 뒤로 한 채 바륵한테 간다."
    USER "뭐지.. 먹구름..?"
    J "비라도 오는건가?"
    KEN "이건 비가 아니다."
    AGARES "녀석이 시작했다."
    "마왕쪽"
    NABE "마왕님 지금 막 무르무르의 강령술 준비가 끝났습니다."
    DAV "좋다!! 강령술을 시작해라!"
    "무르무르 쪽"
    MU "[[이곳에서 죽어 잠들어 버린 영혼들이여 깨어나라]"
    NARR "무르무르의 주문이 시작되자 어둠이 하늘을 뒤덮인다."
    MU "[[나의 부름에 깨어난 영혼들이여 지금부터 나를 도와 나의 적 그리고 마왕님의 적인\n인간들을 죽여라.]"
    NARR "무르무르의 주문이 끝나자 땅에서 유령 들이 나타나고\n무르무르가 명령하자 유령들이 인간들의 몸에 들어가자,\n유령에 씐 인간들이 고통에 몸부림치다가 하나둘씩 죽어 나가기 시작했다."
    "그 시각 교황쪽"
    NARR "교황은 땅을 발로 차면서 말한다."
    G "하찮은 벌레 놈들이!! 발악하고 있어! 지금부터는 내가 나서야겠어 [[빛의 축복]"
    NARR "교황이 능력을 쓰자 어두웠던 하늘이 다시 밝아졌고, 인간들에 씐 유령들이 사라졌다."
    G "[[신의 손길]"
    NARR "교황이 능력을 쓰자 인간들의 마력이 크게 상승한다."
    "마왕 쪽"
    MU "죄송합니다. 대 성공 까지는 아니었습니다."
    DAV "무슨 소리인가 무르무르 이 정도면 대성공이다."
    MU "칭찬 감사합니다. 마왕님"
    NABE "마왕님 빠른속도로 무언가가 접근하고있습니다!!"
    DAV "나도 느꼈다. 저 정도의 마력 정도면 교황이겠지"
    NABE "이동합니까?"
    DAV "당연하지! 우리는 전선으로 간다!"
    "아가레스 쪽"
    
    return
label cancel_fire:
    return
