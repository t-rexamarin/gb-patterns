from front_controllers.base_fc import current_date
from views import IndexView, AboutView, PricingView

routes = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/pricing/': PricingView(),
}

fronts = (current_date, )
