
# Child Page
Gives the child page list of the selected page.
## Individual Setup
This `MD Essential Blocks` plugin contains many blocks. To use the `MD Child Page block` individually follow the below steps.
>⚠️ Note: All the paths given are respective to this plugin please do the required changes if needed
>👉You can copy the code directly from the file if required. Or can follow the below steps to add files
## 🎯  STEPS TO FOLLOW :
 #### Copy the `child-page` block folder to folder which contains all of your blocks.
#### 1.   Add the index.php file from the child-page folder into your main index php file. As per the example below.
    #Adding the path to the file
    require_once plugin_dir_path( __FILE__)."blocks/dynamic/child-page/index.php";
#### 2 .  Add the block.js file from the child-page folder into your main block js file. As per the example below.
    # Adding the path to the file
    import './blocks/static/child-page/block';
#### 3 . At last import the required CSS files to your main CSS file.
```sh
# Adding the path to the file
@import "../blocks/static/child-page/css/editor.css";
```
```sh
# Adding the path to the file
@import "../blocks/static/child-page/css/front.css";
```
## 📦Features
#### :gear: Block Settings:
- **Number of columns**: Slider to control number of cloumns.
- **Select parent Page**: Dropdown to select parent page.
- **Order By**: Dropdown to select the acending or decending order of the posts.
