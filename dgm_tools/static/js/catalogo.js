$(document).ready(function(){
    $(document).keypress(
        function(eventHandler){
         if (eventHandler.which === "13") {
            eventHandler.preventDefault();
          }
    });

    var $pagination = $(".pagination");
    var prevPagination = $pagination.html();
    var post_list = [];
    var page_results = [];

    var template_post = `<div class="col-md-6 post-item">
        <div class="inner">
                <a href="/soluciones-abiertas/herramientas/{{slug}}">
                    {{#image}}
                        <img alt="{{title}}" src="{{image}}">
                    {{/image}}
                    {{^image}}
                        <img alt="{{title}}" src="https://datos.gob.mx/public/img/uploads/5a3801925f14526e00dcdd64/f6GxgdxBGHm13LbR.png">
                    {{/image}}
                </a>

                <a class="tag no-cursor">
                    <span class="tag-icon tag-nula"></span>
                </a>

            </div>

            <div class="post-info">
                <h3>
                    <a alt="{{title}}" href="/soluciones-abiertas/herramientas/{{slug}}">{{title}}</a>
                </h3>
                <p class="excerpt hidden-xs hidden-sm ">{{description}}</p>
                <p class="category">
                    <a class="no-cursor">{{category}}</a>
                </p>
                <p class="author">Coordinación de Estrategia Digital Nacional (CEDN)
                    <a alt="{{title}}" class="read-more" href="/soluciones-abiertas/herramientas/{{slug}}">Leer más</a>
                </p>
            </div>
    </div>`;

    function paginate (array, page_size, page_number) {
        --page_number; // because pages logically start with 1, but technically with 0
        return array.slice(page_number * page_size, (page_number + 1) * page_size);
    }

    function callAPIPosts(){
        Mustache.parse(template_post);
        $('.server-posts').hide();

        var filtros = "";
        var dificultad_herramienta = $("#dificultad-herramienta").val();
        var tipo_herramienta = $("#tipo-herramienta").val();
        var titulo_herramienta = $("#titulo-herramienta").val();
        var PAGE_SIZE = 10;

        if(titulo_herramienta.trim()){
            filtros = "title=" + encodeURIComponent(titulo_herramienta.trim());
        }

        if(tipo_herramienta.trim()){
            if(filtros.trim()){
               filtros = filtros + "&";
            }

            filtros += "category=" + tipo_herramienta.trim();
        }

        if(dificultad_herramienta.trim()){
            if(filtros.trim()){
                filtros = filtros + "&";
             }

             filtros += "level=" + dificultad_herramienta.trim();
        }

        if(!filtros){
            $(".pagination-server").show();
            $(".pagination").hide();
            $(".api-posts").hide();
            $(".server-posts").show();
            return false;
        }

        $.get("/soluciones-abiertas/api/posts/?" + filtros).done(function(response){
            $(".api-posts").html('');
            post_list = response.results;
            page_results = response.results;

            if(response.results.length === 0){
                return false;
            }
            if(response.results.length > PAGE_SIZE){
                page_results = paginate(post_list, PAGE_SIZE, 1);
            }

            for(var x=0; x < page_results.length; x++){
                if(x % 2 === 0 && x > 0){
                    $(".api-posts").append("<div class='clearfix'></div>");
                }
                var rendered = Mustache.render(template_post, page_results[x]);
                $(".api-posts").append(rendered);
            }

            $(".pagination-server").hide();
            $pagination.html('');

            if($pagination.twbsPagination){
                $pagination.twbsPagination("destroy");
            }

            $pagination.twbsPagination({
                totalPages: Math.ceil(response.results.length / PAGE_SIZE),
                cssStyle: '',
                first: '<span aria-hidden="true">&laquo;</span>',
                last: '<span aria-hidden="true">&raquo;</span>',
                prev: '<span aria-hidden="true">‹</span>',
                next: '<span aria-hidden="true">›</span>',
                onPageClick: function (evt, page) {
                    $(".api-posts").html('');
                    var page_list = paginate(post_list, PAGE_SIZE, page);

                    for(var x=0; x < page_list.length; x++){
                        if(x % 2 === 0 && x > 0){
                            $(".api-posts").append("<div class='clearfix'></div>");
                        }
                        var rendered = Mustache.render(template_post, page_list[x]);
                        $(".api-posts").append(rendered);
                    }
                }
            });
            $pagination.show();
            $(".api-posts").show();
        }).fail(function(response){
            console.log(response);
            $pagination.hide();
            $(".pagination-server").show();
            $(".server-posts").show();
            $(".api-posts").hide();
        });
    }

    $("#titulo-herramienta").keypress(function(eventHandler){
        if(eventHandler.which === 13){
            // callAPIPosts();
            return false;
        }
    });


    $('.search-button').click(function(event){
        // callAPIPosts();
        return false;
    });
});