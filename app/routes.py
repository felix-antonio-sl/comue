from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import Paciente, Atencion
from .utils import procesar_historia, procesar_detalle_atencion

main = Blueprint('main', __name__)
@main.route('/')
def lista_atenciones():
    atenciones = Atencion.query.order_by(Atencion.creado_en.desc()).all()
    return render_template('atenciones.html', atenciones=atenciones)
@main.route('/crear_atencion', methods=['GET', 'POST'])
def crear_atencion():
    if request.method == 'POST':
        run = request.form['run']
        paciente = Paciente.query.filter_by(run=run).first()
        if not paciente:
            paciente = Paciente(run=run)
            db.session.add(paciente)
            db.session.commit()
        atencion = Atencion(paciente_id=paciente.id)
        db.session.add(atencion)
        db.session.commit()
        flash('Atención creada exitosamente.', 'success')
        return redirect(url_for('main.lista_atenciones'))
    return render_template('crear_atencion.html')
@main.route('/detalle_atencion/<string:atencion_id>', methods=['GET', 'POST'])
def detalle_atencion(atencion_id):
    atencion = Atencion.query.get_or_404(atencion_id)
    paciente = atencion.paciente

    if request.method == 'POST':
        if 'actualizar_historia' in request.form:
            paciente.historia = request.form['historia']
            db.session.commit()
            flash('Historia actualizada correctamente.', 'success')
        elif 'actualizar_detalle' in request.form:
            atencion.detalle = request.form['detalle']
            db.session.commit()
            flash('Detalle de atención actualizado correctamente.', 'success')
        elif 'procesar_historia_bruto' in request.form:
            texto_bruto = request.form['historia_bruto']
            historia_actualizada = procesar_historia(paciente.historia or '', texto_bruto)
            paciente.historia = historia_actualizada
            db.session.commit()
            flash('Historia procesada y actualizada.', 'success')
        elif 'procesar_detalle_bruto' in request.form:
            texto_bruto = request.form['detalle_bruto']
            detalle_actualizado = procesar_detalle_atencion(
                paciente.historia or '', atencion.detalle or '', texto_bruto)
            atencion.detalle = detalle_actualizado
            db.session.commit()
            flash('Detalle de atención procesado y actualizado.', 'success')
        return redirect(url_for('main.detalle_atencion', atencion_id=atencion_id))

    return render_template(
        'detalle_atencion.html',
        atencion=atencion,
        paciente=paciente
    )