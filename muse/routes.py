from muse import m_app, m_db
from .models import EmployeeMuse
from .forms import AddEmployee, UpdateEmployee

from flask import redirect, render_template, url_for, flash


@m_app.route('/')
def home_page():
    # print(employees)
    return render_template('index.html')


@m_app.route('/create/', methods=['GET', 'POST'])
def create_page():
    add_emp = AddEmployee()
    if add_emp.validate_on_submit():
        fname = add_emp.first_name.data
        lname = add_emp.last_name.data
        addr = add_emp.address.data
        sal = add_emp.salary.data

        check_emp = EmployeeMuse.query.filter_by(address=addr).first()

        if check_emp is None:
            new_employee = EmployeeMuse(fname, lname, addr, sal)
            m_db.session.add(new_employee)
            m_db.session.commit()

            flash(message="Employee added successfully.")
            return redirect(url_for('home_page'))

        else:
            flash(message="This employee already exists.")
            return redirect(url_for('home_page'))

    return render_template('create_record.html', a_form=add_emp)


@m_app.route('/about/')
def about_page():
    return render_template('about.html')


@m_app.route('/read/')
def view_page():
    employees = EmployeeMuse.query.all()

    return render_template('view_page.html', emp_all=employees)


@m_app.route('/update/<int:e_id>/', methods=['GET', 'POST'])
def update_page(e_id):
    employee = EmployeeMuse.query.filter_by(employee_id=e_id).first()

    update_form = UpdateEmployee()

    if update_form.validate_on_submit():
        new_fname = update_form.f_name.data
        new_lname = update_form.l_name.data
        new_addr = update_form.address.data
        new_sal = update_form.salary.data

        if employee.first_name == new_fname and employee.last_name == new_lname and employee.address == new_addr and employee.salary == new_sal:
            flash(message="Record is unchanged. Values are the same.")
            # m_db.session.rollback()
        else:
            employee.first_name = new_fname
            employee.last_name = new_lname
            employee.address = new_addr
            employee.salary = new_sal

            # m_db.session.add(employee)
            m_db.session.commit()

            flash(message="Employee Record has been updated.")
            return redirect(url_for('home_page'))

    return render_template('update_record.html', u_form=update_form, emp=employee)


@m_app.route('/delete/<int:e_id>/')
def delete_record(e_id):
    employee = EmployeeMuse.query.filter_by(employee_id=e_id).first()

    m_db.session.delete(employee)
    m_db.session.commit()

    flash(message=f"Record [{employee.first_name} {employee.last_name}] deleted successfully.")
    return redirect(url_for('home_page'))
