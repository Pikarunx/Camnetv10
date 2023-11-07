#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#instagram.com/mahmut_y0r

import requests, re , colorama
colorama.init()
print("""
\033[1;32m\033[1;32m 
███╗   ███╗ █████╗ ██╗  ██╗███╗   ███╗██╗   ██╗████████╗  ██╗   ██╗ ██████╗ ██████╗ 
████╗ ████║██╔══██╗██║  ██║████╗ ████║██║   ██║╚══██╔══╝  ╚██╗ ██╔╝██╔═████╗██╔══██╗
██╔████╔██║███████║███████║██╔████╔██║██║   ██║   ██║      ╚████╔╝ ██║██╔██║██████╔╝
██║╚██╔╝██║██╔══██║██╔══██║██║╚██╔╝██║██║   ██║   ██║       ╚██╔╝  ████╔╝██║██╔══██╗
██║ ╚═╝ ██║██║  ██║██║  ██║██║ ╚═╝ ██║╚██████╔╝   ██║███████╗██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝    ╚═╝╚══════╝╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                
\033[1;32m                                                                        @alphanetwork1p 
\033[1;33m2) \033[1;35mJapan                        \033[1;33m32) \033[1;35mFinland               \033[1;33m62) \033[1;35mNicaragua
\033[1;33m3) \033[1;35mItaly                        \033[1;33m33) \033[1;35mChina                 \033[1;33m63) \033[1;35mMalta
\033[1;33m1) \033[1;35mUnited States                \033[1;33m31) \033[1;35mMexico                \033[1;33m61) \033[1;35mMoldova
\033[1;33m4) \033[1;35mKorea                        \033[1;33m34) \033[1;35mChile                 \033[1;33m64) \033[1;35mTrinidad And Tobago
\033[1;33m5) \033[1;35mFrance                       \033[1;33m35) \033[1;35mSouth Africa          \033[1;33m65) \033[1;35mSoudi Arabia
\033[1;33m6) \033[1;35mGermany                      \033[1;33m36) \033[1;35mSlovakia              \033[1;33m66) \033[1;35mCroatia
\033[1;33m7) \033[1;35mTaiwan                       \033[1;33m37) \033[1;35mHungary               \033[1;33m67) \033[1;35mCyprus
\033[1;33m8) \033[1;35mRussian Federation           \033[1;33m38) \033[1;35mIreland               \033[1;33m68) \033[1;35mPakistan
\033[1;33m9) \033[1;35mUnited Kingdom               \033[1;33m39) \033[1;35mEgypt                 \033[1;33m69) \033[1;35mUnited Arab Emirates
\033[1;33m10) \033[1;35mNetherlands                 \033[1;33m40) \033[1;35mThailand              \033[1;33m70) \033[1;35mKazakhstan
\033[1;33m11) \033[1;35mCzech Republic              \033[1;33m41) \033[1;35mUkraine               \033[1;33m71) \033[1;35mKuwait
\033[1;33m12) \033[1;35mTurkey                      \033[1;33m42) \033[1;35mSerbia                \033[1;33m72) \033[1;35mVenezuela
\033[1;33m13) \033[1;35mAustria                     \033[1;33m43) \033[1;35mHong Kong             \033[1;33m73) \033[1;35mGeorgia
\033[1;33m14) \033[1;35mSwitzerland                 \033[1;33m44) \033[1;35mGreece                \033[1;33m74) \033[1;35mMontenegro
\033[1;33m15) \033[1;35mSpain                       \033[1;33m45) \033[1;35mPortugal              \033[1;33m75) \033[1;35mEl Salvador
\033[1;33m16) \033[1;35mCanada                      \033[1;33m46) \033[1;35mLatvia                \033[1;33m76) \033[1;35mLuxembourg
\033[1;33m17) \033[1;35mSweden                      \033[1;33m47) \033[1;35mSingapore             \033[1;33m77) \033[1;35mCuracao
\033[1;33m18) \033[1;35mIsrael                      \033[1;33m48) \033[1;35mIceland               \033[1;33m78) \033[1;35mPuerto Rico
\033[1;33m19) \033[1;35mIran                        \033[1;33m49) \033[1;35mMalaysia              \033[1;33m79) \033[1;35mCosta Rica
\033[1;33m20) \033[1;35mPoland                      \033[1;33m50) \033[1;35mColombia              \033[1;33m80) \033[1;35mBelarus
\033[1;33m21) \033[1;35mIndia                       \033[1;33m51) \033[1;35mTunisia               \033[1;33m81) \033[1;35mAlbania
\033[1;33m22) \033[1;35mNorway                      \033[1;33m52) \033[1;35mEstonia               \033[1;33m82) \033[1;35mLiechtenstein
\033[1;33m23) \033[1;35mRomania                     \033[1;33m53) \033[1;35mDominican Republic    \033[1;33m83) \033[1;35mBosnia And Herzegovia
\033[1;33m24) \033[1;35mViet Nam                    \033[1;33m54) \033[1;35mSloveania             \033[1;33m84) \033[1;35mParaguay
\033[1;33m25) \033[1;35mBelgium                     \033[1;33m55) \033[1;35mEcuador               \033[1;33m85) \033[1;35mPhilippines
\033[1;33m26) \033[1;35mBrazil                      \033[1;33m56) \033[1;35mLithuania             \033[1;33m86) \033[1;35mFaroe Islands
\033[1;33m27) \033[1;35mBulgaria                    \033[1;33m57) \033[1;35mPalestinian           \033[1;33m87) \033[1;35mGuatemala
\033[1;33m28) \033[1;35mIndonesia                   \033[1;33m58) \033[1;35mNew Zealand           \033[1;33m88) \033[1;35mNepal
\033[1;33m29) \033[1;35mDenmark                     \033[1;33m59) \033[1;35mBangladeh             \033[1;33m89) \033[1;35mPeru
\033[1;33m30) \033[1;35mArgentina                   \033[1;33m60) \033[1;35mPanama                \033[1;33m90) \033[1;35mUruguay
\033[1;33m91) \033[1;35mExtra                       \033[1;33m92) \033[1;35mAndorra               \033[1;33m93) \033[1;35mAntigua And Barbuda
\033[1;33m94) \033[1;35mArmenia                     \033[1;33m95) \033[1;35mAngola                \033[1;33m96) \033[1;35mAustralia
\033[1;33m97) \033[1;35mAruba                       \033[1;33m98) \033[1;35mAzerbaijan            \033[1;33m99) \033[1;35mBarbados
\033[1;33m100) \033[1;35mBonaire                    \033[1;33m101) \033[1;35mBahamas              \033[1;33m102) \033[1;35mBotswana
\033[1;33m103) \033[1;35mCongo                      \033[1;33m104) \033[1;35mIvory Coast          \033[1;33m105) \033[1;35mAlgeria
\033[1;33m106) \033[1;35mFiji                       \033[1;33m107) \033[1;35mGabon                \033[1;33m108) \033[1;35mGuernsey
\033[1;33m109) \033[1;35mGreenland                  \033[1;33m110) \033[1;35mGuadeloupe           \033[1;33m111) \033[1;35mGuam
\033[1;33m112) \033[1;35mGuyana                     \033[1;33m113) \033[1;35mHonduras             \033[1;33m114) \033[1;35mJersey
\033[1;33m115) \033[1;35mJamaica                    \033[1;33m116) \033[1;35mJordan               \033[1;33m117) \033[1;35mKenya
\033[1;33m118) \033[1;35mCambodia                   \033[1;33m119) \033[1;35mSaint Kitts          \033[1;33m120) \033[1;35mCayman Islands
\033[1;33m121) \033[1;35mLaos                       \033[1;33m122) \033[1;35mLebanon              \033[1;33m123) \033[1;35mSri Lanka
\033[1;33m124) \033[1;35mMorocco                    \033[1;33m125) \033[1;35mMadagascar           \033[1;33m126) \033[1;35mMacedonia
\033[1;33m127) \033[1;35mMongolia                   \033[1;33m128) \033[1;35mMacao                \033[1;33m129) \033[1;35mMartinique
\033[1;33m130) \033[1;35mMauritius                  \033[1;33m133) \033[1;35mNamibia              \033[1;33m132) \033[1;35mNew Caledonia
\033[1;33m133) \033[1;35mNigeria                    \033[1;33m134) \033[1;35mQatar                \033[1;33m135) \033[1;35mReunion
\033[1;33m136) \033[1;35mSudan                      \033[1;33m137) \033[1;35mSenegal              \033[1;33m138) \033[1;35mSuriname
\033[1;33m139) \033[1;35mSao Tome And Principe      \033[1;33m140) \033[1;35mSyria                \033[1;33m141) \033[1;35mTanzania
\033[1;33m142) \033[1;35mUganda                     \033[1;33m143) \033[1;35mUzbekistan           \033[1;33m144) \033[1;37mSaint Vincent And The Grenadines
\033[1;33m145) \033[1;37mBenin


""")

try:
    print()
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                 "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                 "MD", "NI", "MT", "TT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                 "-" , "AD", "AG", "AM", "AO", "AU", "AW", "AZ", "BB", 
                 "BQ", "BS", "BW", "CG", "CI", "DZ", "FJ", "GA", "GG", "GL",
                 "GP", "GU", "GY", "HN", "JE", "JM", "JO", "KE", "KH", "KN",
                 "KY", "LA", "LB", "LK", "MA", "MG", "MK", "MN", "MO", "MQ",
                 "MU", "NA", "NC", "NG", "QA", "RE", "SD", "SN", "SR", "ST",
                 "SY", "TZ", "UG", "UZ", "VC","BJ", ]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 145+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;32m", ip)
except:
    pass
finally:
    print("\033[1;33m")
    exit()
