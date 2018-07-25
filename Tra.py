from enthought.traits.api import HasTraits, Str, Int


class SimpleEmployee(HasTraits):
    first_name = Str
    last_name = Str
    department = Str

    employee_number = Str
    salary = Int


sam = SimpleEmployee()
sam.configure_traits()

print(sam.department)
