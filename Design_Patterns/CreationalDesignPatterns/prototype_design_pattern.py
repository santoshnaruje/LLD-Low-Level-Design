import copy


class Prototype:

    def clone(self):
        return copy.deepcopy(self)


class Document(Prototype):
    def __init__(self, title, font, color, size,layout):
        self.title = title
        self.font = font
        self.color = color
        self.size = size
        self.layout = layout

    def __str__(self):
        return f'{self.title} {self.font} {self.color} {self.size}'

if __name__ == '__main__':
    base_template = Document(
        title="Company Report",
        font="Arial",
        color="blue",
        size=12,
        layout="Standard"
    )
    print(base_template)

    # Clone for sales report
    sales_report = base_template.clone()
    sales_report.title = "Sales Report"
    print(sales_report)

    # Clone for HR report
    hr_report = base_template.clone()
    hr_report.title = "HR Report"
    hr_report.font = "Times New Roman"
    print(hr_report)

    print(id(base_template))
    print(id(sales_report))
    print(id(hr_report))
