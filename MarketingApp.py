class Product:
	def __init__(self, product_code, product_category, product_title, product_price, product_quantity):
		self.product_code = int(product_code)
		self.product_category = product_category
		self.product_title = product_title
		self.product_price = float(product_price)
		self.product_quantity = float(product_quantity)

	def to_dictionary(self):
		return {"Category":self.product_category, 
				"Title":self.product_title,
				"Price":self.product_price,
				"Quantity":self.product_quantity}


class Shop:
	def __init__(self):
		self.product_list = {}

	def add_product(self, product_code, product):
		self.product_list.setdefault(product_code, product)

	def check_product(self, product_code):
		if product_code in self.product_list:
			return True

		return False

	def search_product(self, product_code):
		if self.check_product:
			print("Product Detail:")
			print(f"Product Code: {product_code}")
			
			for k,v in self.product_list.get(product_code).items():
				print(f"{k}: {v}")
		else:
			print("Invalid product code!")
		
	def update_product(self, product_code):
		self.search_product(product_code)

		if self.check_product(product_code):

			try:
				if "yes" == input("Do you want to update the product category? Enter yes or no: "):
					self.product_list.get(product_code)["Category"] = input("Please enter new category: ")

				if "yes" == input("Do you want to update the product title? Enter yes or no: "):
					self.product_list.get(product_code)["Title"] = input("Please enter new title: ")

				if "yes" == input("Do you want to update the product price? Enter yes or no: "):
					self.product_list.get(product_code)["Price"] = float(input("Please enter new price: "))

				if "yes" == input("Do you want to update the product quantity? Enter yes or no: "):
					self.product_list.get(product_code)["Quantity"] = float(input("Please enter new quantity: "))

			except:
				print("Invalid input!")
			
	def buy_product(self, product_code, product_quantity):
		if self.product_list.get(product_code).get("Quantity") > 0:
			if product_quantity <= self.product_list.get(product_code).get("Quantity"):
				total_price = product_quantity * self.product_list.get(product_code).get("Quantity") * 1.15

				if product_quantity > 30:
					total_price *= .7
				elif product_quantity > 20:
					total_price *= .8
				elif product_quantity > 10:
					total_price *= .9
				
				print(f"The total price to pay is $ {total_price}.")
				self.product_list.get(product_code)["Quantity"] -= product_quantity	


def main():
	shop = Shop()

	while True:
		print("\nPlease select one of the following options:")
		print("1. Add Product")
		print("2. Search Product")
		print("3. Update Product")
		print("4. Buy Product")
		print("5. Exit")
		user_choice = input("Please enter 1, 2, 3, 4, or 5: ")

		if user_choice == "1":
			add_more_products = "yes"

			while add_more_products == "yes":

				while True:
					user_code = input("Enter product code: ")

					if user_code.isdigit():
						break

				if shop.check_product(int(user_code)):
					continue

				user_category = input("Enter product category: ")
				user_title = input("Enter product title: ")
				
				while True:
					user_price = input("Enter product price: ")

					if user_price.isdigit():
						break
				
				while True:
					user_quantity = input("Enter product quantity: ")

					if user_quantity.isdigit():
						break

				product_to_add = Product(user_code, user_category, user_title, user_price, user_quantity)
				shop.add_product(int(user_code), product_to_add.to_dictionary())

				add_more_products = input("Do you want to add more products? yes or no: ")
		elif user_choice == "2":
			code_exists = False

			while not code_exists:
				while True:
					code_to_search = input("Enter product code: ")

					if code_to_search.isdigit():
						break

				if shop.check_product(int(code_to_search)):
					shop.search_product(int(code_to_search))
					code_exists = True
		elif user_choice == "3":

			while True:
				code_to_update = input("Enter product code: ")
				
				if code_to_update.isdigit():
					if shop.check_product(int(code_to_update)):
						break

			shop.update_product(int(code_to_update))

		elif user_choice == "4":

			while True:
				code_to_buy = input("Please enter code of the product you want to buy: ")

				if code_to_buy.isdigit():
					break

			if not shop.check_product(int(code_to_buy)):
				continue

			stock_validation = False

			while not stock_validation:

				while True:
					quantity_to_buy = input("Please enter quantity to buy: ")

					if quantity_to_buy.isdigit():
						break

				if shop.product_list.get(int(code_to_buy)).get("Quantity") >= float(quantity_to_buy):
					shop.buy_product(int(code_to_buy), float(quantity_to_buy))
					stock_validation = True
				else:
					print("Not enough stock to buy.")
		elif user_choice == "5":
			break

if __name__ == "__main__":
	main()
