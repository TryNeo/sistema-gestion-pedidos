import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.db.models import Sum

from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from apps.dbd.modelos.estructura_model_pedido import Pedido,PedidoItem

class ReportePedidoPdf(LoginRequiredMixin,View):
    def get (self, request,*args,**kwargs):
        try:
            today = timezone.now()
            pedido = Pedido.objects.all()
            total_pedido = Pedido.objects.filter().count()
            total_general = Pedido.objects.all().aggregate(Sum('total'))
            total_todo = total_general['total__sum']
            context = {
                    'user': self.request.user,
                    'today':today,
                    'datos':{'empresa':'Asoproteseu S.A','telefono':'099-8364-0298','ruc':'1790004104001'},
                    'pedido':pedido,
                    'total_general':total_todo,
                    'total_pedido':total_pedido
            }
            template = get_template("reportes/pedido_report.html")
            html = template.render(context)
            response = HttpResponse(content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename="reporte_pedidos.pdf"'

            pisa_status = pisa.CreatePDF(
            html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('dbd:pedido_list'))

@login_required(login_url="/")
@permission_required("dbd.view_pedido",login_url="dbd:privilegios")
def ReportePedidoClientePdf(request,id_pedido):
    try:
        today = timezone.now()        
        pedido = Pedido.objects.filter(id_pedido=id_pedido).first()
        if pedido:
            pedido_detalle = PedidoItem.objects.filter(pedido=id_pedido)
        else:
            pedido_detalle={}

        
        context = {
            'pedido_detalle': pedido_detalle,
            'pedido':pedido,
            'user': request.user,
            'today':today,
            'datos':{'empresa':'Asoproteseu S.A','telefono':'099-8364-0298','ruc':'1790004104001'},
            'request': request
        }
        template = get_template('reportes/pedido_report_cliente.html')
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="report_pedido_cliene.pdf"'

        pisaStatus = pisa.CreatePDF(
        html, dest=response)
        return response
    except:
        pass
    return HttpResponseRedirect(reverse_lazy('dbd:pedido_list'))

