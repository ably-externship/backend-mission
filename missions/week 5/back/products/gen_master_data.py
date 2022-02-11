from .models import *


def gen_master(apps, schema_editor):
    # Category
    Category(name='아우터').save()
    Category(name='상의').save()
    Category(name='원피스/세트').save()
    Category(name='팬츠').save()
    Category(name='스커트').save()
    Category(name='트레이닝').save()
    Category(name='가방').save()
    Category(name='신발').save()
    Category(name='패션소품').save()
    Category(name='홈웨어').save()
    Category(name='주얼리').save()
    Category(name='언더웨어').save()
    Category(name='빅사이즈').save()
    Category(name='비치웨어').save()
    Category(name='라이프').save()
    Category(name='뷰티').save()
    Category(name='디지털/핸드폰').save()

    # 더미 데이터
    product = Product(market_id=1, name='카라 숏코트', display_name='핸드메이드보다 부드러운, 버터 카라 숏코트;4col', category_id=1,
                      original_price=46000, discounted_price=43000,
                      detail='여유로운 핏으로 지금부터 쭈-욱 착용하기 좋은 러블리한 숏코트를 데려왔어요 :)')
    product.save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Yellow',
                  option2_display_name='옐로우').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Black',
                  option2_display_name='블랙').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Beige',
                  option2_display_name='베이지').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Cream',
                  option2_display_name='크림').save()
    product = Product(market_id=1, name='무지긴팔티', display_name='내몸에딱 옆트임 레이어드 무지긴팔티 3color', category_id=2,
                      original_price=12800, discounted_price=9800,
                      detail='레이어드 했을때 가장이쁜 +5cm길이감으로 제작되어 S,M,L 선택시 내몸에딱 맞는 길이선택OK')
    product.save()
    ProductOption(product=product, option1_name='S', option1_display_name='S', option2_name='White',
                  option2_display_name='화이트').save()
    ProductOption(product=product, option1_name='S', option1_display_name='S', option2_name='Gray',
                  option2_display_name='그레이').save()
    ProductOption(product=product, option1_name='S', option1_display_name='S', option2_name='Black',
                  option2_display_name='블랙').save()
    ProductOption(product=product, option1_name='M', option1_display_name='M', option2_name='White',
                  option2_display_name='화이트').save()
    ProductOption(product=product, option1_name='M', option1_display_name='M', option2_name='Gray',
                  option2_display_name='그레이').save()
    ProductOption(product=product, option1_name='M', option1_display_name='M', option2_name='Black',
                  option2_display_name='블랙').save()
    ProductOption(product=product, option1_name='L', option1_display_name='L', option2_name='White',
                  option2_display_name='화이트').save()
    ProductOption(product=product, option1_name='L', option1_display_name='L', option2_name='Gray',
                  option2_display_name='그레이').save()
    ProductOption(product=product, option1_name='L', option1_display_name='L', option2_name='Black',
                  option2_display_name='블랙').save()
    product = Product(market_id=1, name='셔츠 원피스', display_name='뷔스티에 체인 리본 셔츠 원피스', category_id=3, original_price=34800,
                      discounted_price=24800, detail='셔츠 원피스와 뷔스티에가 레이어드된 듯한 디자인의 원피스예요.')
    product.save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Brown',
                  option2_display_name='브라운').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Black',
                  option2_display_name='블랙').save()
    product = Product(market_id=1, name='와이드팬츠', display_name='스프링 이지핏 밴딩트레이닝 와이드팬츠 4color', category_id=4,
                      original_price=12400, discounted_price=9400, detail='체형에구애없이 누구나 데일리하게 즐겨입기좋은 이지핏 밴딩와이드팬츠 소개드려요')
    product.save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Black',
                  option2_display_name='블랙').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Gray',
                  option2_display_name='그레이').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='White',
                  option2_display_name='백염').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Cream',
                  option2_display_name='크림').save()
    product = Product(market_id=1, name='테니스 스커트', display_name='푸딘 하이틴 플리츠 테니스 스커트', category_id=5,
                      original_price=29000, discounted_price=15370, detail='누구나 예쁘게 착용이 가능한 하이틴 무드의 플리츠 스커트에요 :)')
    product.save()
    ProductOption(product=product, option1_name='S', option1_display_name='S', option2_name='Black',
                  option2_display_name='블랙').save()
    ProductOption(product=product, option1_name='S', option1_display_name='S', option2_name='Gray',
                  option2_display_name='그레이').save()
    product = Product(market_id=1, name='집업 와이드팬츠 세트', display_name='이지핏 트레이닝 투웨이크롭집업 와이드팬츠세트 4color', category_id=6,
                      original_price=36800, discounted_price=26800, detail='크롭기장의 후드집업과 와이드핏의 밴딩팬츠 모두 활용도 높은 아이템이에요')
    product.save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Black',
                  option2_display_name='블랙').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Gray',
                  option2_display_name='그레이').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Cream',
                  option2_display_name='크림').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Oatmeal',
                  option2_display_name='오트밀').save()
    product = Product(market_id=1, name='레더 크로스백', display_name='플랜 미니멀 스퀘어 버클 레더 크로스백 데일리 베이직 스트릿 심플 가방',
                      category_id=7, original_price=22900, discounted_price=9900,
                      detail='군더더기 없이 깔끔하고 심플한 디자인에 넉넉한 수납력을 자랑하는 심플하고 미니멀한 무지 레더 크로스백이에요 .')
    product.save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Black',
                  option2_display_name='블랙').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='White',
                  option2_display_name='화이트').save()
    product = Product(market_id=1, name='롱 삭스부츠', display_name='머스티 스판 싸이하이 스웨이드 롱 삭스부츠', category_id=8,
                      original_price=29900, discounted_price=19300, detail='어디에 매치해도 잘어울리는 컬러로 베이직 & 데일리로 매치해요!')
    product.save()
    ProductOption(product=product, option1_name='225', option1_display_name='225', option2_name='Black',
                  option2_display_name='스웨이드블랙').save()
    ProductOption(product=product, option1_name='230', option1_display_name='230', option2_name='Black',
                  option2_display_name='스웨이드블랙').save()
    ProductOption(product=product, option1_name='235', option1_display_name='235', option2_name='Black',
                  option2_display_name='스웨이드블랙').save()
    ProductOption(product=product, option1_name='240', option1_display_name='240', option2_name='Black',
                  option2_display_name='스웨이드블랙').save()
    ProductOption(product=product, option1_name='245', option1_display_name='245', option2_name='Black',
                  option2_display_name='스웨이드블랙').save()
    ProductOption(product=product, option1_name='250', option1_display_name='250', option2_name='Black',
                  option2_display_name='스웨이드블랙').save()
    ProductOption(product=product, option1_name='255', option1_display_name='255', option2_name='Black',
                  option2_display_name='스웨이드블랙').save()
    product = Product(market_id=2, name='집게핀 모음', display_name='데일리포인트 집게핀 모음', category_id=9, original_price=1800,
                      discounted_price=1400, detail='머리에 포인트를 줄 수 있는 예쁜 집게핀!')
    product.save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Black',
                  option2_display_name='블랙').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Brown',
                  option2_display_name='브라운').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='White',
                  option2_display_name='화이트').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Pink',
                  option2_display_name='핑크').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Purple',
                  option2_display_name='퍼플').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Orange',
                  option2_display_name='오렌지').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Ivory',
                  option2_display_name='아이보리').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Yellow',
                  option2_display_name='옐로우').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Blue',
                  option2_display_name='블루').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Gold',
                  option2_display_name='골드').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Silver',
                  option2_display_name='실버').save()
    ProductOption(product=product, option1_name='FREE', option1_display_name='FREE', option2_name='Rainbow',
                  option2_display_name='레인보우').save()
    product = Product(market_id=2, name='큐빅 진주 스터드', display_name='19종 세트 귀걸이 925은침 데일리 큐빅 진주 스터드', category_id=10,
                      original_price=4900, discounted_price=4900, detail='작은 사이즈로 매일매일 부담없이 데일리로 착용 가능한 세트 귀걸이 모음입니다!')
    product.save()
    ProductOption(product=product, option1_type='PIECE', option1_name='6P', option1_display_name='6P',
                  option2_name='큐빅귀걸이', option2_display_name='뉴 큐빅귀걸이').save()
    ProductOption(product=product, option1_type='PIECE', option1_name='5P', option1_display_name='6P',
                  option2_name='블랙 하트', option2_display_name='빈티지 블랙 하트').save()
    ProductOption(product=product, option1_type='PIECE', option1_name='12P', option1_display_name='6P',
                  option2_name='브라운 리본곰', option2_display_name='브라운 리본곰').save()
    ProductOption(product=product, option1_type='PIECE', option1_name='6P', option1_display_name='6P',
                  option2_name='큐빅링', option2_display_name='큐빅링').save()
    ProductOption(product=product, option1_type='PIECE', option1_name='12P', option1_display_name='6P',
                  option2_name='블랙십자가', option2_display_name='블랙십자가').save()
    ProductOption(product=product, option1_type='PIECE', option1_name='6P', option1_display_name='6P',
                  option2_name='골드 진주콕', option2_display_name='골드 진주콕').save()
