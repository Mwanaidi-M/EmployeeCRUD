from muse import m_db


class EmployeeMuse(m_db.Model):
    employee_id = m_db.Column(m_db.Integer, primary_key=True)
    first_name = m_db.Column(m_db.String(length=50), nullable=False)
    last_name = m_db.Column(m_db.String(length=50), nullable=False)
    address = m_db.Column(m_db.String(length=125), nullable=False, unique=True)
    salary = m_db.Column(m_db.Integer, nullable=False)

    def __init__(self, fname, lname, addr, sal):
        self.first_name = fname
        self.last_name = lname
        self.address = addr
        self.salary = sal

    def __repr__(self):
        return f"Employee: {self.first_name}"

