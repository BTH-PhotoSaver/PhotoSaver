% include('header.tpl', title=name)

% setdefault('error_messages', [])
% for m in error_messages:
  <div class="alert alert-danger" role="alert">
    {{m}}
  </div>
% end

<section class="container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h1>Share Your Memories.</h1><br>
        <form method="POST" action="/upload" enctype="multipart/form-data">
          <div class="mb-3">
            <label for="formGroupCategoryInput">Image Title</label>
            <input type="text" class="form-control" id="formGroupTitleInput" placeholder="Enter a title for the image" name="title">
          </div>
          <div class="mb-3">
            <label for="formGroupCategoryInput">Image Description</label>
            <textarea class="form-control" id="formGroupDescriptionTextArea" rows="3" placeholder="Enter a description for the image" name="description"></textarea>
          </div>
          <div class="mb-3">
            <label for="formGroupFileInput">Select File</label><br>
            <input type="file" class="form-control-file" id="formGroupFileInput" placeholder="Select the file" name="uploaded_file">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </section>

% include('footer.tpl', title=name)
