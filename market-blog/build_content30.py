# -*- coding: utf-8 -*-
# [시장 브리핑 30] 주식·금·코인·부동산 조건표
import json, html, os, shutil
EM_COLOR="#F03030"; EM_FONT="나눔스퀘어"; ST_COLOR="#1F4E79"
CSS_FONT="'나눔스퀘어', NanumSquare, sans-serif"
HL_Y="linear-gradient(transparent 55%, #fff3a0 55%)"; HL_G="linear-gradient(transparent 55%, #d8f5b8 55%)"
def P(*runs):
    out=[]
    for r in runs: out.append({"text":r} if isinstance(r,str) else r)
    return {"type":"paragraph","runs":out}
def SRC(t): return {"type":"paragraph","runs":[{"text":t,"fontSize":15}]}
def B(t):  return {"text":t,"bold":True}
def EM(t): return {"text":t,"bold":True,"color":EM_COLOR,"font":EM_FONT}
def HL(t): return {"text":t,"bold":True,"bgColor":"yellow"}
def HG(t): return {"text":t,"bold":True,"bgColor":"green"}
BL={"type":"blank"}; DV={"type":"divider"}
def ST(t): return {"type":"sectionTitle","text":t,"color":ST_COLOR}
def Q(t,style="quotation_line"): return {"type":"quote","style":style,"text":t}
def IMG(f,c): return {"type":"image","file":f,"caption":c}
LOCH="소장: 미국 의회도서관 하이스미스 아카이브 · 퍼블릭 도메인"
LOCP="소장: 미국 의회도서관 인쇄·사진부 · 공개 제한 없음"

blocks=[
 Q("금리는 모든 자산의 중력이다 — 다만 같은 중력이 자산마다 다른 길로 닿는다"),
 BL,
 P("4부작의 마지막입니다. 27편에서 중국과 일본, 28편에서 미국, 29편에서 한국의 금리와 부채를 봤습니다. 오늘은 그 위에 놓인 네 자산, ",B("주식·금·코인·부동산"),"이 지금 어디에 있고, 앞으로 어떤 조건에서 어느 쪽으로 움직이는지를 정리합니다."),
 BL,
 P("먼저 분명히 해 둘 것이 있습니다. 이 글은 ",HL("어느 자산을 사라거나 팔라는 글이 아닙니다"),". 금리가 자산에 닿는 길을 원자료로 그리고, 조건이 이러면 이쪽, 저러면 저쪽이라는 조건문을 적는 글입니다. 조건이 맞는지는 9월 16일, 18일, 11월 4일이 결정합니다."),
 DV,

 ST("① 성적표 — 금리가 오른 해에 무엇이 떨어졌나"),
 IMG("images/01-scorecard.png","2026년 9월 10일 기준 고점 대비 등락 (자료: 스툭, FRED, 한국거래소, 한국부동산원)"),
 BL,
 P("2026년은 미국 30년물이 5.3%까지 오른 해입니다. 그 해에 가장 크게 떨어진 자산은 ",EM("금과 비트코인"),"입니다. 금은 1월 29일 5,379달러 고점에서 7월 3,977달러까지 26% 빠졌다가 지금 4,317달러, 고점 대비 20% 아래입니다. 비트코인은 2025년 10월 12만 2천 달러에서 올 6월 6만 달러로 반 토막 났다가 7만 7천 달러, 고점 대비 37% 아래입니다."),
 BL,
 P("반대로 주식은 거의 안 빠졌습니다. S&P500은 8월 13일 7,799 고점에서 2.7% 아래이고, 코스피는 9월 7일 6,995에서 0.4% 아래입니다. 부동산은 올랐습니다. 서울 아파트가 올해 누적 7.3%, 미국 주택이 전년 대비 1.5%입니다. ",B("금리 상승기에 실물과 이익이 있는 자산은 버티고, 이자를 안 주는 자산이 먼저 맞았습니다"),". 이 순서가 이 글의 출발점입니다."),
 DV,

 ST("② 금리는 어떤 길로 닿나"),
 IMG("images/06-circuit.png","장기금리가 네 자산에 닿는 세 갈래 길 (작도: 직접 제작)"),
 BL,
 P("길은 셋입니다. 첫째는 ",B("할인율(discount rate)"),"입니다. 주식과 부동산의 값은 미래 이익을 현재값으로 바꾼 것이고, 그 환율이 장기금리입니다. 금리가 오르면 먼 미래의 이익일수록 싸집니다. AI 설비투자처럼 회수가 먼 사업이 금리에 예민한 이유입니다."),
 BL,
 P("둘째는 ",B("실질금리와 달러"),"입니다. 금은 이자가 없으니 물가를 뺀 실질금리가 오르면 금을 들고 있는 기회비용이 커지고, 달러가 강하면 달러로 값을 매기는 금은 내려갑니다. 올해 금이 26% 빠진 건 이 길이었습니다. 셋째는 ",B("달러 유동성"),"입니다. 코인은 이익도 이자도 없어서 오직 돈이 얼마나 풀려 있느냐에 반응합니다. 28편의 베이시스 거래 8,300억 달러가 풀리면 가장 먼저 흔들리는 자산입니다."),
 BL,
 P("한국에는 길이 하나 더 있습니다. 미국 장기금리가 국고채로, 국고채가 주택담보대출 금리로, 그것이 서울 아파트로 이어지는 길입니다. 29편에서 본 대로 ",HL("한국은 그 청구서가 정부가 아니라 가계에 갑니다"),"."),
 DV,

 ST("③ 주식 — 이익이 금리를 이기고 있다, 아직은"),
 IMG("images/07-nyse.jpg","뉴욕증권거래소 객장, 1980~2006년 촬영. "+LOCH),
 P("S&P500이 고점 근처에 있는 이유는 워시 의장이 잭슨홀에서 말한 숫자 하나로 설명됩니다. 기업 이익이 전년 대비 20% 넘게 늘고 설비투자가 9% 늘었습니다. 할인율이 올라도 분자인 이익이 더 빨리 크면 주가는 버팁니다. 코스피는 여기에 반도체 수출 209%와 원화 강세 13%가 얹혔습니다."),
 BL,
 P("문제는 이 버팀이 조건부라는 점입니다. 시나리오 ㄱ, 재무부가 11월 4일 장기물 발행을 줄여 30년물이 5% 아래로 내려오면 할인율이 내려가고 먼 이익일수록 다시 비싸집니다. 시나리오 ㄴ, 9월 16일과 18일에 연준과 일본은행이 같이 올리고 베이시스 거래가 풀리면 ",HG("2024년 8월 5일이 반복됩니다"),". 그날 코스피는 8.77%, 닛케이는 12.4% 빠졌습니다. 반도체 비중이 큰 코스피가 S&P500보다 더 흔들리는 구조는 그때와 같습니다."),
 DV,

 ST("④ 금 — 두 엔진이 꺼진 자리"),
 IMG("images/08-gold.jpg","알래스카 노메의 한 은행에 쌓인 125만 달러어치 금괴와 사금, 1906년 6월. "+LOCP),
 IMG("images/02-gold.png","금 현물 가격 2025~2026 (자료: 스툭 XAUUSD)"),
 BL,
 P("20편에서 중앙은행 외환보유고에서 금이 미국 국채를 30년 만에 앞질렀다고 썼습니다. 그 흐름은 지금도 유효하지만 가격은 다른 이야기입니다. 1월 5,379달러는 실질금리 하락과 달러 약세, 두 엔진이 같이 돌 때의 값이었습니다. 3월부터 미국 물가가 3.7%에 머물고 금리가 오르자 실질금리가 반등했고, 금은 넉 달 만에 26% 빠졌습니다. 8월 25일 4,659달러까지 되올랐다가 잭슨홀 뒤 다시 4,300대입니다."),
 BL,
 P("조건문은 이렇습니다. 시나리오 ㄱ이면 두 엔진이 재가동되고 1월 고점 재도전이 열립니다. 시나리오 ㄴ이면 7월 저점 3,977달러를 다시 시험합니다. 다만 금에는 예외 조항이 하나 있습니다. 28편의 금 재평가 카드처럼 ",B("미국 국채 자체의 신뢰가 흔들리는 국면"),"이면 금리가 올라도 금이 오릅니다. 2022년 영국 길트 위기 때 파운드 기준 금값이 그랬습니다."),
 DV,

 ST("⑤ 코인 — 유동성의 온도계"),
 IMG("images/03-btc.png","비트코인 가격 2025~2026 (자료: 스툭 BTCUSD)"),
 BL,
 P("비트코인은 2025년 10월 7일 12만 2천 달러에서 올 6월 25일 6만 달러까지 51% 빠졌습니다. 같은 기간 금이 오르고 있었으니 둘은 같은 자산이 아닙니다. 코인은 달러 유동성이 줄면 금보다 먼저, 더 크게 빠지고, 8월에 6만 4천에서 8만 2천으로 반등한 것도 재무부가 바이백을 두 배로 늘린다고 발표한 8월 19일 전후 주간과 겹칩니다."),
 BL,
 P("조건문입니다. 시나리오 ㄱ이면 8월 반등의 연장이고, 시나리오 ㄴ이면 6만 달러 재시험입니다. 한 가지 역설이 있습니다. 19편에서 본 달러 스테이블코인은 준비금을 미국 단기국채로 두어야 하므로, ",HL("코인 시장이 커질수록 미국 단기채 수요가 늘어납니다"),". 베센트가 스테이블코인을 밀어 온 이유이고, 코인 가격과 무관하게 이 수요는 남습니다."),
 DV,

 ST("⑥ 부동산 — 한국은 강남이 먼저 꺾였다"),
 IMG("images/04-seoul-apt.png","서울·노원·강남 아파트 주간 변동률 2026 (자료: 한국부동산원)"),
 BL,
 P("서울 아파트는 올해 누적 7.3% 올랐지만 안을 들여다보면 갈라져 있습니다. 강남은 8월 들어 주간 변동률이 마이너스로 돌아섰고, 노원은 0.5%로 올해 최고입니다. 11편에서 2026년이 2021년이 아니라 2007년을 닮았다고 썼는데, 그해도 강남이 먼저 멈추고 외곽이 뒤늦게 키를 맞추다 2008년을 맞았습니다. 지금 주간 그래프가 그 순서를 그리고 있습니다."),
 BL,
 P("여기에 29편의 청구서가 붙습니다. 8월 주택담보대출이 4조 3천억 늘었고 한국은행은 10월 22일 3.25%를 열어 두었습니다. 국고채 10년물 4.45%는 주담대 고정금리의 기준입니다. 시나리오 ㄱ이면 국고채가 미국을 따라 내려와 한은의 인상 압력이 줄고, 시나리오 ㄴ이면 ",B("주담대 금리 상승과 강남 조정이 외곽으로 번지는 경로"),"가 열립니다. 미국은 모기지 30년 고정이 6.76%로 올해 최고이고, 케이스실러 주택가격은 전년 대비 1.5%로 거의 멈춰 있습니다."),
 DV,

 ST("⑦ 표로 정리하면"),
 IMG("images/05-matrix.png","두 시나리오 × 네 자산 조건표 (작도: 직접 제작)"),
 BL,
 P("이 표는 예측이 아니라 조건문입니다. 왼쪽 칸이 맞으려면 11월 4일 재무부가 장기물 발행을 줄여야 하고, 오른쪽 칸이 맞으려면 9월 16일과 18일 두 중앙은행이 같이 올려야 합니다. 28편에서 본 대로 탄약은 재무부 쪽이 많고 시간은 중앙은행 쪽이 유리합니다. 그래서 순서는 ",HG("9월에 오른쪽이 먼저 시험되고 11월에 왼쪽이 답한다"),"가 될 가능성이 큽니다."),
 BL,
 P("4부작을 한 줄로 줄이면 이렇습니다. 미국은 정부 빚을 낮은 금리로 굴리려 하고, 일본은 밖에 빌려준 돈을 거둬들이고, 중국은 넘치는 예금을 쓸 곳을 못 찾고, 한국은 반도체로 번 돈으로 가계 빚의 이자를 내고 있습니다. 네 자산은 그 네 나라의 결정이 만나는 자리에서 값이 매겨집니다. 다음 확인은 9월 16일 밤입니다."),
 DV,

 SRC("자료: 스툭(XAUUSD·BTCUSD 종가), 세인트루이스 연준 FRED(SP500·MORTGAGE30US·CSUSHPINSA·DGS30), 한국거래소 코스피 종가(9/7·9/10), 한국부동산원 주간 아파트가격동향(2026.1.5~8.24), 금융위원회 2026년 8월 가계대출 동향, 연준 이사회 워시 의장 잭슨홀 연설(2026.8.28), 연준 FEDS Notes(2026.6.22)."),
 SRC("사진: 미국 의회도서관 인쇄·사진부 — 하이스미스 아카이브(뉴욕증권거래소 객장), 인쇄·사진부(1906년 알래스카 노메 금괴). 모두 공개 제한 없음으로 표시된 자료."),
 SRC("이 글은 투자 권유가 아니며 특정 자산이나 종목의 매수·매도를 추천하지 않습니다. 시나리오는 조건문이며 예측이 아닙니다. 투자 판단과 책임은 투자자 본인에게 있습니다."),
]

def runs_of(b): return b.get("runs",[]) if b.get("type")=="paragraph" else []
text="".join(r["text"] for b in blocks for r in runs_of(b))+"".join(b.get("text","") for b in blocks if b.get("type") in ("sectionTitle","quote"))
chars=len(text); bolds=[r for b in blocks for r in runs_of(b) if r.get("bold")]
ratio=sum(len(r["text"]) for r in bolds)/max(chars,1)
quotes=[b for b in blocks if b.get("type")=="quote"]; hls=[r for b in blocks for r in runs_of(b) if r.get("bgColor")]
ems=[r for b in blocks for r in runs_of(b) if r.get("color")]; imgs=[b for b in blocks if b.get("type")=="image"]
for b in blocks: assert len([r for r in runs_of(b) if r.get("color")])<=1
assert 2500<=chars<=7000, f"글자수 {chars}"; assert len(bolds)>=8; assert ratio<=0.10, f"굵기비중 {ratio:.3f}"
assert len(quotes)>=1; assert 3<=len(hls)<=8, f"형광펜 {len(hls)}"
for r in hls:
    n=len(r["text"]); assert 6<=n<=45, f"형광펜 길이 {n}: {r['text']}"; assert '(' not in r["text"] and ')' not in r["text"]
print(f"글자수 {chars} / 굵게 {len(bolds)} ({ratio*100:.1f}%) / 색 {len(ems)} / 형광펜 {len(hls)} / 인용구 {len(quotes)} / 이미지 {len(imgs)}")

SRCDIR="/home/user/market-blog/re51"
for d in ("pkg50","pkg50t"):
    p=f"/home/user/market-blog/{d}/images"; shutil.rmtree(f"/home/user/market-blog/{d}",ignore_errors=True); os.makedirs(p)
    for b in imgs: f=os.path.basename(b["file"]); shutil.copy(f"{SRCDIR}/{f}", f"{p}/{f}")
TITLE="금리가 오른 해, 금 −20%·비트코인 −37%·서울 아파트 +7% — 주식·금·코인·부동산은 어디로 가나, 두 시나리오 조건표 [시장 브리핑 30]"
TAGS=["금값전망","비트코인전망","코스피전망","부동산전망","금리인상"]
META={"title":TITLE,"category":"시장 브리핑","tags":TAGS,"series":{"name":"시장 브리핑","no":30},"charCount":chars}
json.dump({"meta":META,"blocks":blocks},open("/home/user/market-blog/pkg50/content.json","w"),ensure_ascii=False,indent=1)
json.dump({"title":TITLE,"category":"시장 브리핑","tags":TAGS,"publishMode":"draft","coupang":False},open("/home/user/market-blog/pkg50t/meta.json","w"),ensure_ascii=False,indent=1)
def esc(t): return html.escape(t)
out=[f"<h1>{esc(TITLE)}</h1>"]
for b in blocks:
    t=b["type"]
    if t=="paragraph":
        s=""
        for r in b["runs"]:
            x=esc(r["text"]); st=[]
            if r.get("bold"): st.append("font-weight:700")
            if r.get("color"): st.append(f"color:{r['color']};font-family:{CSS_FONT}")
            if r.get("bgColor")=="yellow": st.append(f"background:{HL_Y}")
            if r.get("bgColor")=="green": st.append(f"background:{HL_G}")
            if r.get("fontSize"): st.append(f"font-size:{r['fontSize']}px;color:#888")
            s+=f"<span style=\"{';'.join(st)}\">{x}</span>" if st else x
        out.append(f"<p>{s}</p>")
    elif t=="sectionTitle": out.append(f"<h2 style=\"color:{ST_COLOR}\">{esc(b['text'])}</h2>")
    elif t=="quote": out.append(f"<blockquote>{esc(b['text'])}</blockquote>")
    elif t=="image": out.append(f"<figure><img src=\"{b['file']}\" style=\"max-width:100%\"><figcaption>{esc(b['caption'])}</figcaption></figure>")
    elif t=="divider": out.append("<hr>")
    elif t=="blank": out.append("<p>&nbsp;</p>")
open("/home/user/market-blog/pkg50t/content.html","w").write("<meta charset='utf-8'><body style=\"max-width:760px;margin:0 auto;font-family:sans-serif;line-height:1.9\">"+"\n".join(out)+"</body>")
print("packaged: pkg50 / pkg50t")
