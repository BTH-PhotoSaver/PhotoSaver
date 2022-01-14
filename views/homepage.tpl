% include('header.tpl', title=name)
<style type="text/css">
.card-columns {
  @include media-breakpoint-only(lg) {
    column-count: 4;
  }
  @include media-breakpoint-only(xl) {
    column-count: 5;
  }
}
</style>

<main>
  <section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h1 class="fw-light">PhotoSaver</h1>
        <p class="lead text-muted">Upload some photos of your best memories to save and present them to others!</p>
        <p>
          <a href="/upload" class="btn btn-primary my-2">Upload your own image</a>
        </p>
      </div>
    </div>
  </section>
  <div class="row grid" data-masonry='{"percentPosition": true }'>
    % for item in items:
    <div class="col-sm-6 col-lg-4 mb-4">
      <div class="card">
        <img class="card-img-top" src="https://icc-proj-images.s3.amazonaws.com/{{item.get('imagepath')}}" alt="{{item.get('title')}}">
        <div class="card-body">
          <h5 class="card-title">{{item.get('title')}}</h5>
          <p class="card-text">{{item.get('description')}}</p>
          <p class="card-text"><small class="text-muted">Uploaded at {{item.get('uploaded')}}</small></p>
        </div>
      </div>
    </div>
    % end
  </div>

</main>

% include('footer.tpl')
